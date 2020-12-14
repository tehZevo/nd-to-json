# nd-to-json

Converts nd arrays (lists of lists and NumPy arrays) to and from a json-encodable data structure.

## Now with 50% more compression.
Compression format (by default) is:
```
base64(gzip([
  number_of_dimensions,
  dim_0_size, dim_1_size, ..., dim_n_size,
  data_0, data_1, ..., data_n
]))
```
