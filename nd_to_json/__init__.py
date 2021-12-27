import numpy as np
import zlib
import base64
import io
import orjson

def nd_to_json(r, method="orjson"):
  if method == "orjson":
    return orjson.dumps(r, option=orjson.OPT_SERIALIZE_NUMPY).decode("utf8")
  if method == "np_save":
    b = io.BytesIO()
    np.save(b, r)
    b.seek(0)
    b = b.read()
    b = base64.encodebytes(b)
    b = b.decode('utf8')
    return b
  #plain method
  return {"data": r.flatten().tolist(), "shape": r.shape}

def json_to_nd(r, method="orjson"):
  if method == "orjson":
    return orjson.loads(r)
  if method == "np_save":
    b = r.encode('utf8')
    b = base64.decodebytes(b)
    b = io.BytesIO(b)
    b = np.load(b)
    return b
  #plain method
  return np.reshape(r["data"], r["shape"])
