n = 4
space = 2 * (n - 1)

for i in range(1,n+1):
    
    for j in range(1, i+1):
        print(j, end="")
    
    for j in range(space):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")
   
    print()

    space = space - 2