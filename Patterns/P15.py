#approach 1

n = 5

for i in range(n):
    for ch in range(ord('A'), ord('A') + (n - i)):
        print(chr(ch), end="")
    print()


#approach 2

'''
n = 5

for i in range(n - 1, -1, -1):
    for ch in range(ord('A'), ord('A') + i + 1):
        print(chr(ch), end="")
    print()
'''


#approach 3

'''
n = 5

for i in reversed(range(n)):
    for ch in range(ord('A'), ord('A') + i + 1):
        print(chr(ch), end="")
    print()
'''




