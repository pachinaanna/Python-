def modify_list(list):
    # print(list)
    to_delete = []
    for i in list:
        # print(str(i))
        # print(str(i) + ' ' + str(i / 2))
        if i == 0 or i % 2 != 0:
            to_delete.append(i)
    for i in to_delete:
        list.remove(i)

    for i in range(len(list)):
        list[i] = list[i]//2
    return list

if __name__ == '__main__':
    print(modify_list([1, 2, 3, 4, 6, 8]))
    print(modify_list([0,0,0]))
    print(modify_list([4,6,8]))
    print(modify_list([1, 2, 3]))
    print(modify_list([]))
    print(modify_list([1,3,5,7]))