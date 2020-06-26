lst = [int(i) for i in input().split()]
x = int(input())
j = 0
for i in lst:
    if i == x:
        print(j, end=' ')
    j += 1
if x not in lst:
    print('Отсутствует')
