numeros = [2, 4, 5, 67, 2, 56, 87]

re1 = list(map(lambda x: x * 2, numeros)) # lambda
re2 = [x * 2 for x in numeros] # list comprehension
re3 = [x * 2 for x in numeros if x % 2 == 0] # list comprehension com If
re4 = [x * 2 if x % 2 == 0 else x / 2 for x in numeros] # list comprehension com If e Else

print(re1)
print(re2)
print(re3)
print(re4)