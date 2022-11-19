max_num = int(input())
str_num = []

for i in range(1, 10000):
    if i**2 > max_num:
        break
    str_num.append(str(i**2))
print(*str_num)
