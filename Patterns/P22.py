n = 4

for i in range(2*n - 1):
    for j in range(2*n-1):

        top = i
        left = j
        right = (2*n-2) - i
        down = (2*n-2) - j

        nearst_distance = min(top, left, right, down)

        print(n - nearst_distance, end="")

    print()

