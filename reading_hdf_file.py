import time
import h5py

scan_number = 55

file_path = f"/nsls2/data/hex/proposals/commissioning/pass-318884/tomography/raw_data/scan_000{scan_number}/proj_00000.hdf"
key = "entry/data/data"
hdf_object = h5py.File(file_path, 'r')
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
