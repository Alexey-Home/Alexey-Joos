import numpy as np


n = int(input())
k = int(input())
arr = []
new_arr = []

for i in range(n):
    arr.append(i)


while n % k != 0:
    n -= 1
    k -= 1
    tmp = []
    for j in range(n//k):
        tmp.append(arr[j])
        arr.pop(j)
    new_arr.append(tmp)


print(new_arr)
