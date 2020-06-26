def counter_war_and_peace(line):
    dict_1 = {}
    for word in [lower_word.lower() for lower_word in line.split()]:
        if word not in dict_1:
            dict_1[word] = 1
        else:
            dict_1[word] = dict_1[word] + 1
    print(dict_1)


# counter_war_and_peace(input())

if __name__ == '__main__':
    counter_war_and_peace('aa abC aa ac abc bcd a')
    counter_war_and_peace('a A a')