def counter(input):
    line = input
    max_index = len(line) - 1
    current_index = 0
    counter = 0
    previos_letter = ''
    result = ''
    while current_index <= max_index:
        current_letter = line[current_index]

        if current_letter == previos_letter or previos_letter == '':
            counter += 1
        if current_letter != previos_letter and previos_letter != '':
            result += previos_letter + str(counter)
            counter = 1

        if current_index == max_index:
            result += current_letter + str(counter)

        current_index += 1
        previos_letter = current_letter

    print(result)


if __name__ == '__main__':
    counter("ab")
    counter("aaaabbcaaa")
    counter("abc")
    counter("aabbc")
    counter("aaa")
    counter("a")
    counter("aaaaaaaaaaaa")
