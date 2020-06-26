numbers = [int(i) for i in input().split()]
result = 0
max_index = len(numbers)-1
current_index = 0
if max_index != 0:
    if current_index == 0:
        result = numbers[max_index] + numbers[current_index + 1]
        current_index += 1
        print(result, end=' ')
    while 1 <= current_index < max_index:
        result = numbers[current_index - 1] + numbers[current_index + 1]
        current_index += 1
        print(result, end=' ')
    if current_index == max_index:
        result = numbers[current_index - 1] + numbers[0]
        print(result, end=' ')
if max_index == 0:
    print(numbers[0])

