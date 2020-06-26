a = int(input())
if a >= 10 and a <= 100:
    print(a)
while a <= 100:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break