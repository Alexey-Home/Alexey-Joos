num = []

while True:
    tm_num = int(input())
    if tm_num == 0:
        break
    else:
        num.append(tm_num)

max_num = num[0]

for i in num:
    if max_num < int(i):
        max_num = int(i)

count = 0

for i in num:
    if max_num == int(i):
        count += 1
print(count)
