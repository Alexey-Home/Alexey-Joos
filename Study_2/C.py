N = int(input())
num_arr = []
max_1 = 0
tmp_max_1 = 0

for i in range(N):
    num_arr.append(int(input()))

for i in num_arr:
    if i == 1:
        tmp_max_1 += 1
    else:
        tmp_max_1 = 0
    if tmp_max_1 > max_1:
        max_1 = tmp_max_1

print(max_1)
