import os
import math

path = 'in.txt'
with open(file=path, mode='r') as f:
    size = math.ceil(os.stat(path)[6] / 2)
    output = []

    for i in range(0, size):
        f.seek(0)
        print(f.read())
