import numpy as np

def json_to_nd(r):
    return np.reshape(r["data"], r["shape"])

def nd_to_json(r):
    return {"data": r.flatten().tolist(), "shape": r.shape}
