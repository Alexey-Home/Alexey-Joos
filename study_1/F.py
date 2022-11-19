N = int(input())
chocolate = []
count = 0
count_dol = 0

for i in range(3):
    tmp_chocolate = []
    for j in range(N):
        tmp_chocolate.append(count)
        count += 1
    chocolate.append(tmp_chocolate)

for i in range(3):
    for j in range(N):
        if 0 < i - 1 < count:
            count_dol += 1
        if 0 < i + 1 < count:
            count_dol += 1
        if 0 < j - 1 < count:
            count_dol += 1
        if 0 < j + 1 < count:
            count_dol += 1

print(chocolate)
