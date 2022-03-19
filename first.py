while True:
    try:
        x = int(input("Введите натуральное число: "))
        if x >= 1:
            break
        else:
            print("Вы ввели не натуральное число!")
    except ValueError as err:
        print("Вы ввели не натуральное число!")
k = 0
for i in range(2, x):
    if i % 2 != 0 or i == 2:
        k += 1
print("Количество простых чисел меньше {0}: {1}".format(x, k))


