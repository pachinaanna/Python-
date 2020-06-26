def print_duplicates(line):

    elements = [int(element) for element in line.split()]
    duplicates = []
    for current_index in range(len(elements)):
        el_counter = elements.count(elements[current_index])
        if el_counter > 1 and elements[current_index] not in duplicates:
            duplicates += [elements[current_index]]

    for duplicate in duplicates:
        print(duplicate, end=" ")


print_duplicates(input())

if __name__ == '__main__':
    print_duplicates("1 1 1 2 2 2 2 3")