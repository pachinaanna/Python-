a = str(input())
b = a.upper()
c = b.count('C')
g = b.count('G')
d = len(a)
e = ((c+g) / d) * 100
print(e)