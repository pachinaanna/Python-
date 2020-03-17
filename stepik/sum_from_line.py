def sum(line):

    numbers = [int(numberStr) for numberStr in line.split()]
    current_index = 0
    result = 0
    for current_index in range(len(numbers)):
        result += numbers[current_index]
        current_index += 1
    print(result)

sum(input)
