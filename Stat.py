import numpy as np

f = open("s.txt", "r")

print(f.readline())

temp = [line[:-1] for line in f]

mean = np.mean(temp)
std = np.std(temp)
mini = np.min(temp)
maxi = np.max(temp)
 

print(f"mean = {mean}")
print(f"mean = {std}")
print(f"mean = {mini}")
print(f"mean = {maxi}")
