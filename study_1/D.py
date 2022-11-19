num_arr = []
result = []
tmp_sum_m = 0
sum_m = 0
mir_sum = 0

while True:
    num = input()
    if num == "#":
        break
    num_arr.append(int(num))

min_num = num_arr[0]
max_num = num_arr[0]

for i in num_arr:
    mir_sum += i
    if min_num > i:
        min_num = i
    if max_num < i:
        max_num = i
mir_sum = round(mir_sum/len(num_arr), 3)

for j in range(len(num_arr)):
    tmp_sum_m += num_arr[j]
    if (j + 1) % 3 == 0:
        sum_m += tmp_sum_m % num_arr[j]
        tmp_sum_m = 0
result.append(mir_sum)
result.append(max_num)
result.append(min_num)
result.append(sum_m)
print(*result)






