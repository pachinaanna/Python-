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