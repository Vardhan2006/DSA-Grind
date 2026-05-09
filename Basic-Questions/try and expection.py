#code 1 Try and execption handling
'''
try:
    car = (1, 2, 3, 4 , 5)
    car.add(6, 7)
    print(car)
except:
    print("tuple cannot be modified after created")
'''

#code 2 

'''
try:
    a = int(input("Enter a value: "))
    for i in range(1, 11):
        print(f"{a} x {i} = {a*i}")
except ValueError:
    print("enter an integer")
'''

#code 3

'''
try:
    l = [1, 2, 3, 4, 5]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    n = int(input("Enter a index: "))
    l1 = (1, 2, 7, 9)
    print(l1[n])
finally: 
    print("I love BMW!")
'''

#code 4

'''
try:
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    c = (input("Enter +, -, *, / any one operator:  "))
    match c:
        case "+":
            print("addition is", a + b)
        case "-":
            print("Substraction is", a - b)
        case "*":
            print("Multiplication is", a * b)
        case "/":
            print("Division is", a / b)
except:
    print("There is an error occured")
finally:
    print("This is a practice code")
'''

#code 5 Custom errors

'''
a = (input("Enter a value between 100 and 120: "))

if (a == "quit"):
    print("Its okay")
elif a < 100 or a > 120:
    raise ValueError("There are error in the input!")
else:
    print('okay the number is between 100 and 120')
'''

#code 6


        














        


