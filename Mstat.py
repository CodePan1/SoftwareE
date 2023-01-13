import statistics
import getopt, sys
import numpy as np
 
arr = []
arr1 = []
max = 0
min = 1000
sum = 0

if sys.argv[1] == "stat":
  with open(sys.argv[2]) as f:
    #   while True:
    lines = f.read().splitlines()
        
        # if not lines:
        #       break
for e in lines:
    num = int(e)
    sum += num
    if (num > max):
        max = num
    if (num < min):
        min = num
    arr.append(num)

print("Satistics Summary")

print(sys.argv[2])
print("mean :", np.mean(arr))
print("std :", statistics.stdev(arr))
print("min :", min)
print("max :", max)



# txt2
if sys.argv[1] == "stat":
    with open(sys.argv[3]) as f:
    #   while True:
        lines = f.read().splitlines()
        
        # if not lines:
        #       break
for e in lines:
    num = int(e)
    sum += num
    if (num > max):
        max = num
    if (num < min):
        min = num
    arr1.append(num)

print(sys.argv[3])
print("mean :", np.mean(arr))
print("std :", statistics.stdev(arr))
print("min :", min)
print("max :", max)

    
#combined
new_arr = arr1 + arr
print("combined")
print("mean :", np.mean(new_arr))
print("std :", statistics.stdev(new_arr))
print("min :", min)
print("max :", max)