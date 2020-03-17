a = int(input())
b = int(input())
print (a*b)

X = int(input())
Y = int(input())
print (X*60+Y)

X = int(input())
print(X//60)
print(X%60)

X = int(input())
H = int(input())
M = int(input())
print((X+M+H*60)//60)
print((X+M+H*60)%60)

A = int(input())
B = int(input())
H = int(input())
A <= B
if H < A:
    print('Недосып')
if H > B:
    print('Пересып')
if A <= H <=B:
    print('Это нормально')

n = int(input())
1900 <= n <= 3000
if n%400 == 0 or n%4 == 0 and n%100 != 0:
    print('Високосный')
else:
    print('Обычный')

a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
S = p*(p-a)*(p-b)*(p-c)
print(S**0.5)

x = int(input())
if -15 < x <= 12 or 14 < x < 17 or 19 <= x:
    print('True')
else:
    print('False')

a = float(input())
b = float(input())
c = input('')
if c == 'mod' and b != 0:
    print(a%b)
if c == 'mod' and b == 0:
    print('Деление на 0!')
if c == '+':
    print(a+b)
if c == "-":
    print(a-b)
if c == '/' and b != 0:
    print(a/b)
if c == '/' and b == 0:
    print('Деление на 0!')
if c == '*':
    print(a*b)
if c == 'pow':
    print(a**b)
if c == 'div'and b != 0:
    print(a//b)
if c == 'div' and b == 0:
    print('Деление на 0!')

f = input('')
if  f =='треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    x = (a+b+c)/2
    S = x*(x-a)*(x-b)*(x-c)
    print(S**0.5)
if f == 'прямоугольник':
    a = float(input())
    b = float(input())
    S = a * b
    print(S)
if f == 'круг':
    r = float(input())
    P = 3.14
    S = P * r ** 2
    print(S)


a = int(input())
b = int(input())
c = int(input())
x = (a, b, c)
print(max(x))
print(min(x))
print((a+b+c)-max(x)-min(x))


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


x = int(input())
a = x//100000
b = (x%100000)//10000
c = (x%10000)//1000
d = (x%1000)//100
e = (x%100)//10
f = x%10
if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')

a = int(input())
b = int(input())
c = int(input())
if b <= a >= c:
    M = a
if a < b >= c:
    M = b
if b < c > a:
    M = c
if b >= a <= c:
   m = a
if a > b <= c:
    m = b
if b > c < a:
    m = c
print(M)
print(m)
if M == a and m == b or m == a and M == b or M == c or m == c:
    print(c)
if M == b and m == c or m == b and M == c or M == a or m == a:
    print(a)
else:
    print(b)
    if M == c and m == a or m == c and M == a:
    print(b)


a = int(input())
s = 0
while a != 0:
      i = a
      s += i
      a = int(input())
else:
    print(s)

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

a = int(input())
if a >= 10 and a <= 100:
    print(a)
while a <= 100:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break



a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('', end='\t')
for j in range(c,d+1):
    print(j,end='\t')
print()
for i in range(a,b+1):
    print(i, end='\t')
    for j in range(c,d+1):
        print(i*j, end='\t')
    print()



a = int(input())
b = int(input())
s = 0
p = 0
if a % 3 == 1:
    a+=2
if a % 3 == 2:
    a+=1
for i in range(a,b+1,3):
    s+=i
    p+=1
print(s/p)



a = str(input())
b = a.upper()
c = b.count('C')
g = b.count('G')
d = len(a)
e = ((c+g) / d) * 100
print(e)


line = input
    size = len(line) - 1
    current_index = 0
    next_index = current_index + 1
    counter = 1
    result = ''
    while next_index < size:
        if line[current_index] == line[next_index]:
            while line[current_index] == line[next_index]:
                current_index += 1
                next_index += 1
                counter += 1
                if(next_index == size):
                    break
        b = line[current_index]
        result += str(b)
        result += str(counter)
        if line[current_index] != line[next_index]:
            current_index += 1
            next_index += 1
            counter = 1
            continue
    if next_index == size:
        if line[current_index] == line[next_index]:
            counter += 1
            b = line[current_index]
            result += str(b)
            result += str(counter)
        if line[current_index] != line[next_index]:
            b = line[size]
            result += str(line[current_index])
            result += str(counter)
            result += str(b)
            result += str(counter)
    if size == 0:
        result += str(b)
        result += str(counter)
    print(result)


a = [int(i) for i in input().split()]
current_index = 0
max_index = len(a)-1
result = 0
for current_index in range (max_index+1):
    result += a[current_index]
    current_index += 1
print(result)


a = [int(i) for i in input().split()]
