n = int(input('Enter a Number: '))

# Taking 2 varibales  a and b and storing 0 and 1 because each number is sum of 2 preceding numbers
a = 0
b = 1

for i in range(n):
    print(a, end = " ")

    temp = a + b
    a = b
    b = temp