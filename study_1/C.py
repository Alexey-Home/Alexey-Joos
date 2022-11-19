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
        if tmp_max_1 > max_1:
            max_1 = tmp_max_1
        tmp_max_1 = 0
print(max_1)
