# Top Half

n = 5

for i in range(1, n + 1):
    for j in range(n - i + 1):
        print("*", end="")

    space = 2 * i

    for j in range(2, space):
        print(" ", end="")
    
    space = space + 2

    for j in range(n-i+1, 0, -1):
        print("*", end="")
    
    print()

# Bottom Half

space = 2 * (n - 1)

for i in range(1, n + 1):

    for j in range(i):
        print("*", end="")
    
    for j in range(space):
        print(" ", end="")
       
    for j in range(i, 0, -1):
        print("*", end="")
        
    print()
    
    space = space - 2
    

    