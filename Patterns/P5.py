# Approach 1

n = 5

for i in range(5, 0, -1):
    for j in range(i):
            print("*", end=" ")
    print()


# Approach 2
'''
n = 5

for i in range(1, n + 1):
    for j in range(n - i + 1):
    
        print("*", end=" ")
    print()
'''