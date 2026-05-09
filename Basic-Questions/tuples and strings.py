#code 1 example 1 
#Tuples are unchangeable meaning we can not alter them after creation.
'''
x1 = (1, 2, 3, 4, 5)
x2 = (9, 10, 11, 12, 13, 14, 15)
print(x1)
print(x2)
'''

#code 2 

'''
x = ("virat kohli", 'Rohit sharma')
print(x[0:2])
'''

#code 3

'''
car = ("BMW", "porsche", "Ferrari", "Dodge", "Lamborghini", "mercedes")
print(car[::])
print(car[5])
print(car[:-1])
print(car[6-5])
'''


#code 4 

#if you want to add, remove or change tuple items, then first you must convert the tuple to a list
'''
country = ("India", "germany", "Russia", "Austrialia", "England")
now = list(country)
now.append("Germany") #add item
now.pop(1)            #remove item
now[3] = "Sri lanka"  #change item
country = tuple(now)
print(country)
'''

#code 5 concatenate two tuples

'''
fav = ("BMW", "Lamborgihini")
fav2 = ("Dodge", "Audi")

Awesome = fav + fav2
print(Awesome)
'''

#code 6 Unpack Tuples

'''
info = ("Vardhan", 18, "Scientist")
(name, age, Occupation) = info
print("Name:", name)
print("Age:", age)
print("Occupation:", Occupation)
'''

#code 7 

'''
fauna = ("Hyena", "Lion", "Tiger", "Jaguar", "cheethah", "Shark", "Eagle",)
(*animals, fish, bird) = fauna
print("Animals:", animals)
print("fish:", fish)
print("Bird:", bird)
'''

#code 8   f-strings

'''
car = "my name is {} and I love {}"
name = "Vardhan"
love = "BMW"

print(car.format(name, love)) #method 1

print(f"my name is {name} and I love {love}") #method 2

#string formatting how many numbers should be taken after the decimal 

price = 49.525357
txt = f"indian currrency of {price: .1f} rupees"
print(txt)

'''

# code 9 practice

'''
price = 15000000.232524
car = f"I will buy this BMW of worth {price: .2f} which is a fantastic price"
print(car)
'''

#code 10

'''
print(f"{77*23+9}")
print(type) #string
'''

#code 11 Doc strings and pep 8

#Doc string (it is not a comment)

'''
def calculateGmean(a, b):
    #,,,takes two inputs from the user a and b, then calculates the mean,,,

    mean = (a * b)/(a + b)
    print(mean)
a = 9
b = 8
calculateGmean(a, b)
print(calculateGmean.__doc__)
'''

#code 12 recursion

'''
x = int(input("Enter a value: "))
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*(n-1)
print(factorial(x))
'''


# code 13 fibonacci series

'''
x = int(input("enter a value: "))
def fib(n):
    if(n == 0 or n == 1):
        return n
    else:
        return fib(n-1) + fib(n-2)
for i in range(x):
    print(fib(i))
'''

#code 14 time pass
'''
for i in range(1, 10 + 1):
    print(5, "x", i, "=", 5*i)
'''

# code 15 (rough) Sets numbers cannot be repeat

'''
s = {18, 5, 6, 6}
print(s)
info = {"rohit sharma", 45, True, 5.9, 264 }
print(info)

empty_set = {""}
empty_set = set()
print(type(empty_set))

for value in info:
    print(value)
'''

#code 16 order does not matter

'''
s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 4, 3, 10}
s1.add("18, 17")
print(s1)
print(s1. union(s2))
print(s1. intersection(s2)) #empty set
s1. update(s2)
print(s1)
s1. remove(2) #takes only one arguments
s1. difference(s2) #gives difference type of a - b
print(s1)
'''

#code 17 

'''
car = {"BMW", "porsche", "mercedes", "ferrari"}
car. add("lamborghini")
car. discard("punch EV") #no error
car. remove("mercedes") #gives error
car. pop() #removes last element
car. clear() #delete whole items
#del car #key word
print(car)
'''

#code 18 checking where player is present in info or not 

'''
info = {"rohit sharma", 45, True, 5.9, 264 }

if "rohit sharma" in info:
    print("rohit sharma is present")
else:
    print("rohit sharma is absent")
'''

#code 19 intersection() method returns a new set

'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
'''

#code 20 intersection_update() method updates into the existing set from another set.

'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
'''

#code 21

'''
car = {"BMW", "porsche", "mercedes"}
car1 = {"BMW", "porsche", "ferrari"}
car2 = car.symmetric_difference(car1)
print(car2)
'''
#code 22

'''
car = {"BMW", "porsche", "mercedes"}
car1 = {"BMW", "porsche", "ferrari"}
car2 = car.symmetric_difference(car1)
print(car2)
'''

#code 23

'''
car = {"BMW", "porsche", "mercedes"}
car1 = {"Audi", "lamborghini", "ferrari"}
print(car.isdisjoint(car1))
'''

#code 24

'''
car = {"Audi", "lamborghini", "ferrari"}
car1 = {"lamborghini", "ferrari"}
print(car.issuperset(car1))
print(car1.issubset(car))
'''


# The method related to sets are:-
# 1) union()---->creates a new set with the unique elements from both the sets
# 2)update()----->applied on a set itself and it also adds unique elements from the both the sets into one of the sets
# 3) intersection()----> creates a new set with the common elements from both the sets
# 4)intersection_update()------> applied on a set itself and it also contains the common elements from both the sets
# 5)symmetric_difference--------> creates a new set with the elements from the both the sets that are not common in between
# 6)symmetric_difference_update-------> applied on a set itself and it contains elements from the sets that are not common inj between
# 7)difference------> creates a new set with the elements from a single set that are not common 
# 8) difference_update-----> applied on a set itself and contains elements of a set that are not common
# 9)isdisjoint()---->checks if there are common elements between two sets
# 10)issuperset----> checks if a set is a superset of another set
# 11) issubset-----> checks is a set is subset of another set
# 12)add------> to add a element into a set
# 13) remove-------> to remove an elements from a set, but raises key error if the element is not present in the set
# 14) discard-----> to remove an element from a set, does not raises error if the lement is not present in the set
# 15) del------> not method, a keyword, to delete the complete set
# 16) clear-------> to clear all the elements of a set 
# 17) in keyword used to check if a element is present in the set or not
# 18) pop()-----> to remove a random element from the set and also we can get that element