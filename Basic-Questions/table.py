n = int(input('Enter a Number: '))
for i in range(1, 11):
    if i == 5:
        continue
    print(n, 'X', i, '=', i * n)


    