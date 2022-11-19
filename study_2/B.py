column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())

if abs(column1) == abs(column2) or abs(row1) == abs(row2)\
        or abs(column1 - column2) == abs(row1 - row2):
    print("YES")
else:
    print("NO")

