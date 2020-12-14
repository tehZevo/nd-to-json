import numpy as np
import zlib
import base64

ENDIAN = "<"

def nd_to_json(r, compress=True, do_gzip=True, do_b64=True):
    if compress:
        return encode(serialize(r), do_gzip, do_b64)
    return {"data": r.flatten().tolist(), "shape": r.shape}

def json_to_nd(r, compress=True, do_gzip=True, do_b64=True):
    if compress:
        return deserialize(decode(r, do_gzip, do_b64))
    return np.reshape(r["data"], r["shape"])

def encode(r, do_gzip=True, do_b64=True):
    if do_gzip:
        r = zlib.compress(r)
    r = base64.b64encode(r).decode("utf-8") if do_b64 else r.hex()
    return r

def decode(r, do_gzip=True, do_b64=True):
    r = base64.b64decode(r) if do_b64 else bytearray.fromhex(r)
    if do_gzip:
        r = zlib.decompress(r)
    return r

def serialize(r):
    #data will always be 32bit big endian floats
    r = r.astype(ENDIAN+"f4")
    #convert length of shape to int32 bytes
    lenshape = np.array(len(r.shape), dtype=ENDIAN+"i4").tobytes()
    #convert shape to int32 bytes
    shape = np.array(r.shape, dtype=ENDIAN+"i4").tobytes()
    #convert data to bytes
    r = r.flatten().tobytes()
    #concat
    data = lenshape + shape + r

    return data

def deserialize(r):
    #read lenshape
    lenshape = int(np.frombuffer(r[:4], dtype=ENDIAN+"i4"))
    #read shape
    shape = np.frombuffer(r[4:4+lenshape*4], dtype=ENDIAN+"i4")
    #read data
    data = np.frombuffer(r[4+lenshape*4:], dtype=ENDIAN+"f4")
    #reshape data
    data = np.reshape(data, shape)

    return data
