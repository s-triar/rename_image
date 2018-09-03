import os
n = 32
path = "D:\\FOTO DATA SKRIPSI\\"
for i in range(n):
    t = i+1
    r = os.path.join(path, '2'+str(t))
    if t < 10:
        r = os.path.join(path, '20'+str(t))
    if not os.path.exists(r):
        os.makedirs(r)
