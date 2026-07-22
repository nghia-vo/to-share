import os
import time
import h5py
import numpy as np

output_path = "/nsls2/data/hex/proposals/commissioning/pass-318884/tmp/test.hdf"
key = "entry/data/data"

depth = 1801
height = 3200
width = 3200

data_shape = (depth, height, width)
data_type = "uint16"

file_base = os.path.dirname(output_path)
if not os.path.exists(file_base):
    try:
        os.makedirs(file_base, exist_ok=True)
    except OSError:
        raise ValueError("Can't create the folder: {}".format(output_path))
try:
    ofile = h5py.File(output_path, 'w')
except Exception as error:
    raise ValueError(f"Error {error}")

data_stream = ofile.create_dataset(key, data_shape, dtype=data_type)

t0 = time.time()
for i in range(depth):
    data_stream[i] = np.random.randint(0, 65535, size=(height, width))
t1 = time.time()

print(f" Done generating simulation data. Time elapsed: {t1-t0}")

hdf_object = h5py.File(output_path, 'r')
hdf_dataset = hdf_object[key]

(depth, height, width) = hdf_dataset.shape

print("====================================================================\n")
print("         Run the script for getting a few slices                     ")
print(f"        Time: {time.ctime(time.time())}                             ")
print("====================================================================\n")

t_start = time.time()

for idx in range(0, height, 100):
    t0 = time.time()
    slice = hdf_dataset[:, idx, :]
    t1 = time.time()
    print(f"- Done slice {idx}. Time elapsed {t1-t0}")

t_stop = time.time()

print("====================================================================\n")
print(f" All done! current time: {time.ctime(time.time())}")
print(f" Total elapsed time: {t_stop - t_start}")
print("====================================================================\n")
