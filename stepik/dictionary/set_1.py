def counter_war_and_peace(line):
    unique_words = set()
    not_unique_words = line.lower().split()
    for i in line.split():
        unique_words.add(i.lower())

    for u_word in unique_words:
        qty = 0
        for nu_word in not_unique_words:
            if u_word == nu_word:
                qty += 1

        print(u_word + ' ' + str(qty))
    return counter_war_and_peace
# counter_war_and_peace(input())





if __name__ == '__main__':
    counter_war_and_peace('aa abC aa ac abc bcd a')
    counter_war_and_peace('a A a')