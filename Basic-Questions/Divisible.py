n = int(input('Enter a Number: '))

if n % 2 == 0 and n % 3 == 0:
    print('Divisible by Both 2 and 3')
elif n % 2 == 0:
    print('Divisible by 2')
elif n % 3 == 0:
    print('Divisible by 3')
else:
    print('Divisible by None')