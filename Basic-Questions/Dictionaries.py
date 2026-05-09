#code 1 dic are ordered

'''
dic = {
    "bhai": "human being",
    "gun": "object"   
}
print(dic["gun"])
'''

#code 2

'''
data = {
    "name": "vardhan",
    "age": "18",
    "occupation": "student",
    "learning python": "true"
}
print(data["learning python"])
print(data.keys())
for key in data.keys():
    print(data[key])
'''

#code 3 

'''
info = {'name':'Karan', 'age':19, 'eligible':True}

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
'''

#code 4

'''
data = {'name':'Daku mangal singh', 'Age':'40', 'occupation':'Daku', 'eligible': 'No'}
print(f"This is old record {data}")
data.update({'Age':41})
data.update({'DOB':1980})
print(data)
'''

#code 5

'''
car1 = {"BMW":10, "ferrari":9.8, "lamborghini":9.5}
car2 = {"nano":3.5, "suzuki":4.9, "punch":0.001}

car1.update(car2)
car1.pop('punch')
car1.popitem() #pops last item
del car2["punch"]
print(car1)
'''

'''
dic = {
"brand" : "Redmi",
"Model" : "10"
}

x = dic.keys()

print(x)


dic["color"] = "White"

print(dic)

print(dic.keys())

print(dic.get("Model"))

print(len(dic))


print(dic.values())

print(dic.items())

if "Model" in dic:
	print("Yes Model is a key in dic")
    

dic["Model"] = "9"

print(dic)


dic.update({"brand": "Vivo"})

print(dic)



dic = {
"brand" : "Redmi",
"Model" : "10",
"Color" : "Green"
}

del dic["brand"]
del dic

dic.clear()

dic.pop("Model")

print(dic)

dic.popitem()
print(dic)



'''






