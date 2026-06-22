def name(i, n):

    if i > n:
        return
    
    print("Vardhan")    # i = current count | n = how many times name should print
    
    name(i + 1, n)      # Time complexity = o(N)  |  space complexity = o(N)

n = 3
name(1, n)

#Revised Once