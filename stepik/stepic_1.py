a = int(input())
b = int(input())
print (a*b)

a = int(input())
b = int(input())
c = int(input())
x = (a, b, c)
print(max(x))
print(min(x))
print((a+b+c)-max(x)-min(x))







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
