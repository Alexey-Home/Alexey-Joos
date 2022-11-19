s = str(input())
k = int(input())
res = ""

if k > 0:
    for i in range(k):
        res += s
elif k < 0:
    k = abs(k)
    len_s = len(s)
    if len_s % k == 0:
        num = int(len_s / k)
        j = 0
        while j+num <= len_s-1:
            if s[j] != s[j+num]:
                res = "NO SOLUTION"
                break
            j += 1
        else:
            for i in range(k-1):
                s = s[num:]
            res = s
    else:
        res = "NO SOLUTION"
else:
    res = "0"

print(res)
