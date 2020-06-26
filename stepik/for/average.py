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