import numpy as np
import time
import json

from nd_to_json import nd_to_json, json_to_nd, serialize, deserialize

def print_hex(bs, n=8):
    bs = bs.hex()
    bs = [bs[i:i+n] for i in range(0, len(bs), n)]
    print(bs)

#tests:
N = 10
TRIALS = 100
DIMS = [1, 2, 3, 4, 5]
B64 = [True, False]
GZIP = [True, False]

def dim_shape(dim):
    return [N for i in range(dim)]

def create_r(dim):
    #return np.random.normal(0, 1, dim_shape(dim))
    return np.zeros(dim_shape(dim))

def do_run(dim, do_b64, do_gzip):
    r = create_r(dim)
    r = nd_to_json(r, compress=True, do_gzip=do_gzip, do_b64=do_b64)

    r = json.dumps(r)
    r = json.loads(r)

    #now decode
    r = json_to_nd(r, compress=True, do_gzip=do_gzip, do_b64=do_b64)

for dim in DIMS:
    print("dim", dim, "values", np.prod(dim_shape(dim)))
    #old method tests
    times = []
    for _ in range(TRIALS):
        start_time = time.time()
        r = create_r(dim)
        r = json.dumps(nd_to_json(r, compress=False))
        r = json_to_nd(json.loads(r), compress=False)
        times.append(time.time() - start_time)
    avg_time = np.mean(times)
    print("OLD", ":", avg_time)

    #new method tests
    for do_b64 in B64:
        for do_gzip in GZIP:
            times = []
            for _ in range(TRIALS):
                start_time = time.time()
                do_run(dim, do_b64, do_gzip)
                times.append(time.time() - start_time)
            avg_time = np.mean(times)
            print("NEW", "do_b64", do_b64, "do_gzip", do_gzip, ":", avg_time)
    print()
