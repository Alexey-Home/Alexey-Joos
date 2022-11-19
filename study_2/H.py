num = 0

while True:
    number = int(input())
    if number % 2 == 0 and number != 0:
        num += 1
    if number == 0:
        print(num)
        break
