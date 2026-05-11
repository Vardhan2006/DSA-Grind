n = 5


for i in range(1, 2*n):

    stars = i

    if i >= n:
        stars = 2*n-i
    
    space = 2* (n - stars)

    for j in range(stars):
        print("*", end="")
    
    for j in range(space):
        print(" ", end="")

    for j in range(stars):
        print("*", end="")

    print()