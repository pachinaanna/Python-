n = int(input())
1900 <= n <= 3000
if n%400 == 0 or n%4 == 0 and n%100 != 0:
    print('Високосный')
else:
    print('Обычный')