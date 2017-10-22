import numpy as np # linear algebra
import h5py # for processing the hdfs datasets
import matplotlib
matplotlib.use('Qt4Agg')
from matplotlib import pyplot as plt
from os import walk, path

mypath = "C:\Users\Aakash\Desktop\gw\input"
files = []
for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend(filenames)
    break
print files
plt.figure(figsize = (14, 6))
i = 0
col = ['r', 'g', 'b', 'k']
for fname in files:
    d = h5py.File(path.join(dirpath, fname), "r")
    strain = list(d['strain'].values())[0]
    plt.plot(strain[...], color= col[i], label = fname, markersize = 1)
    i += 1
    d.close()
plt.legend()
plt.show()