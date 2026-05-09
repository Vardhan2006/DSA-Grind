#code 1 
# pass is used to leave it and continue the code (it wont give error)
'''
def calculateGmean(a, b):

    mean = (a * b)/(a + b)
    print(mean)
a = 9
b = 8
calculateGmean(a, b)
'''

#code 2 Arguments

'''
def average(a = 10, b = 12):
    print("The average is ", (a+b)/2)
average(6)
'''

#code 3 

'''
def name(fname = 'Virat', lname = 'Kohli'):
    print('Hello!', fname, lname)

name('Rohit', 'Sharma',)
'''

#code 4 taking numbers as tuple

'''
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print('average is ', sum/len(numbers))
average(20, 188, 255)
'''

#code 5 Lists
'''
car = [1, 2, 3]
print(car)
print(type(car))
print(car[0])
print(car[1])
print(car[2])
print(car[len(car)-3]) #converting negative indexing into positive indexing 
'''

#code 6 comphrension list

'''
lst = [i for i in range(5)]
print(lst)
'''

#code 7 list methods

'''

l = [1, 2, 3, 4, 5]
print(l)
# l.append(6)
# print(l)
# print(l.index(2))
# l.sort() #sorting in ascending order
# l.reverse()
# print(l.count(1))
l.copy()
l.insert(0, 7)
l.remove(5)
k = [8, 9, 10]
l.extend(k)
l.pop(5)
l.remove(1)
print(type(l))
print(l)

'''

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"








