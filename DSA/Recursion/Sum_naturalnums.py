class solution:

    def sum(self, N):
        
        if N == 1 or N == 0:
            return N
    
        return N + self.sum(N - 1)

N = int(input("Enter N: "))

obj = solution()

print(obj.sum(N))



#Functional Recursion


'''

sum(4)

= 4 + sum(3)

= 4 + (3 + sum(2))

= 4 + (3 + (2 + sum(1)))

= 4 + (3 + (2 + 1))

= 4 + (3 + 3)

= 4 + 6

= 10

'''




#Parameterised Recursion

def sum(i, sum):

    if i < 0:
        print(sum)
        return
    
    sum(i - 1, sum + i)

sum(3, 0)


'''
Dry run

f(3,0)
    ↓
f(2,3)
    ↓
f(1,5)
    ↓
f(0,6)
    ↓
print(6)


'''

#Revised Once