import numpy as np
import time
import json

from nd_to_json import nd_to_json, json_to_nd

#tests:
N = 10
TRIALS = 100
DIMS = [1, 2, 3, 4, 5]
METHODS = ["orjson", "np_save", "plain"]

def dim_shape(dim):
    return [N for i in range(dim)]

def create_r(dim):
    #return np.random.normal(0, 1, dim_shape(dim))
    return np.zeros(dim_shape(dim))

def do_run(dim, method):
    r = create_r(dim)
    r = nd_to_json(r, method)

    r = json.dumps(r)
    r = json.loads(r)

    #now decode
    r = json_to_nd(r, method)

for dim in DIMS:
    print("dim", dim, "values", np.prod(dim_shape(dim)))
    #new method tests
    for method in METHODS:
      times = []
      for _ in range(TRIALS):
        start_time = time.time()
        do_run(dim, method)
        times.append(time.time() - start_time)
      avg_time = np.mean(times)
      print(f"Method: {method}: {avg_time}s")
    print()
