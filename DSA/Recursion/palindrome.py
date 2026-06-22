class Solution:

    def helper(self, n, rev, org):

        if n == 0:
            return org == rev

        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

        return self.helper(n, rev, org)

    def isPalindrome(self, n):

        n = abs(n)

        return self.helper(n, 0, n)


'''

Dry Run

Input: n = 121

Call:

isPalindrome(121)

org = 121
rev = 0

helper(121, 0, 121)

↓

digit = 1
rev = 1
n = 12

helper(12, 1, 121)

↓

digit = 2
rev = 12
n = 1

helper(1, 12, 121)

↓

digit = 1
rev = 121
n = 0

helper(0, 121, 121)

↓

n == 0

return 121 == 121

True

'''

#revised once