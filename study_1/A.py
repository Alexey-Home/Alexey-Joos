import math

str_mum = str(input())
str_mum = str_mum.split(" ")

gip = math.sqrt(int(str_mum[0])**2 + int(str_mum[1])**2)

if gip <= int(str_mum[2]):
    print("YES")
else:
    print("NO")
