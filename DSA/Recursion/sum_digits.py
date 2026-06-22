class Solution:
    def sumOfDigits(self, n):
        # code here
        
        if n == 0:
            return 0
        
        digit = n % 10
                
        n = n // 10
        
            
        return digit + self.sumOfDigits(n)        



"""

sumOfDigits(123)
= 3 + sumOfDigits(12)

= 3 + (2 + sumOfDigits(1))

= 3 + (2 + (1 + sumOfDigits(0)))

= 3 + (2 + (1 + 0)) # Backtracking Starts

= 3 + (2 + 1)

= 3 + 3

= 6

"""

#Revised once
#Revised Twice