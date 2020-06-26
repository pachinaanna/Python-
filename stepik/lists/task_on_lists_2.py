n = int(input())
result = ''
numbers = [i for i in range(n+1)]
for number in numbers[0:n if n < 45 else n]:
    result += str(number) * number
print(numbers[0:n if n < 45 else n])

# for number in numbers:
#     result += str(number) * number
# if n <= 45:
#     for j in range(n):
#         print(result[j], end=' ')
# else:
#     for j in range(45):
#         print(result[j], end=' ')
#     for j in range(45, n+1, 2):
#         print(result[j] + result[j+1], end=' ')

