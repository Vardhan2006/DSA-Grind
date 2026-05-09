# Using Slicing
'''
name = 'Vardhan'
print(name[: : -1])
'''

name = 'Vardhan'
rev = ""

for ch in name:
    rev = ch + rev

print(rev)