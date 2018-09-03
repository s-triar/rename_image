import os
n = 32  # number sub folder
path = "D:\\FOTO DATA SKRIPSI\\"  # path to folder data
for i in range(n):
    t = i+1
    r = os.path.join(path, '0'+str(t))
    if t < 10:
        r = os.path.join(path, '00'+str(t))
    if not os.path.exists(r):
        os.makedirs(r)
