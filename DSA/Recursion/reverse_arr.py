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