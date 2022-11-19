count_student = int(input())

list_student = [[] for x in range(count_student)]

while True:
    value = input()
    if value == "#":
        for i in range(len(list_student)):
            list_student[i].sort(reverse=True)
        break
    value = value.split()
    list_student[int(value[0])].append(int(value[1]))

list_student.sort(key=lambda x: sum(x), reverse=True)

for i in range(len(list_student)):
    print(*list_student[i], end=" ")
