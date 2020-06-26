a = int(input())
b = int(input())
i = 2
if a >= b:
    d = a
    while d % b != 0:
        d = a * i
        i += 1
    else:
        print(d)
if b > a:
    d = b
    while d % a != 0:
        d = b * i
        i += 1
    else:
        print(d)