n = 5

for i in range(n):
    ch = chr(ord('A') + i)

    for j in range(i + 1):
        print(ch, end="")
    print()