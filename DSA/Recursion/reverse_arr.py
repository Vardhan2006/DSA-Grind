#Two Pointer

class Solution:

    def helper(self, arr, left, right):

        if left >= right:
            return

        arr[left], arr[right] = arr[right], arr[left]

        self.helper(arr, left + 1, right - 1)

    def reverseArray(self, arr):

        self.helper(arr, 0, len(arr) - 1)

        return arr


'''

Current Work:
Swap left and right

Smaller Problem:
left + 1
right - 1

Base Condition:
left >= right

'''


# single pointer 

class Solution:

    def helper(self, arr, i):

        n = len(arr)

        if i >= n // 2:
            return

        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

        self.helper(arr, i + 1)

    def reverseArray(self, arr):

        self.helper(arr, 0)

        return arr


'''

Why is it called Single Pointer?

Because we only maintain one pointer:

i = 0 → 1 → 2

The other pointer is computed automatically:

right = n - i - 1

Why is it called Two Pointer?

Because we explicitly maintain:

left = 0 → 1 → 2
right = 4 → 3 → 2

So:

Two Pointer:
left, right

Single Pointer:
i

'''

#revised once