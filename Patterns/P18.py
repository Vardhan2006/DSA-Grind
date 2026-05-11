n = 5

for i in range(n):
    for ch in range(ord('E') - i, ord('E') + 1):
        print(chr(ch), end="")
    print()