n = int(input())
result = []
for i in range(n+1):
    for j in range(i):
        result.append(i)
for number in result[:n]:
    print(str(number), end=' ')
