n = int(input())
0 <= n <= 1000
if n != 12 and n%10 == 2 and n%100 != 12 or n !=13 and n%10 == 3 and n%100 != 13 or n != 14 and n%10 == 4 and n%100 != 14:
    a = 'программиста'
    print(n,a)
elif n != 11 and n%100 != 11 and n%10 == 1:
    a = 'программист'
    print(n,a)
else:
    a = 'программистов'
    print(n, a)