def sum(line):
    numbers = [int(numberStr) for numberStr in line.split()]
    result = 0
    for current_index in range(len(numbers)):
        result += numbers[current_index]
    print(result)


sum(input())


a = [int(i) for i in input().split()]
current_index = 0
max_index = len(a)-1
result = 0
for current_index in range (max_index+1):
    result += a[current_index]
    current_index += 1
print(result)