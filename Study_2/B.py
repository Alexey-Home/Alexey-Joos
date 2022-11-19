str_num = input()
str_num = str_num.split(" ")
year = 0
if len(str_num) != 3:
    print(year)
else:
    vklad = int(str_num[0])
    percent = int(str_num[1])
    max_vklad = int(str_num[2])

    while vklad <= max_vklad:
        per = vklad*(percent/100)
        per = int(per * 100) / 100
        vklad = vklad + per
        year += 1
    print(year)


