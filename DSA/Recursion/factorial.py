class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        # code here
        
        if n == 0 or n == 1:
            return 1
        
        return n * self.factorial(n-1)



'''
Dry run if n = 5

5 * (5 - 1)
5 * 4 * (4 - 1)
5 * 4 * 3 * (3 - 1)
5 * 4 * 3 * 2 * (2 - 1)
5 * 4 * 3 * 2 * 1 (1 - 1) ====> from here it backtracks
5 * 4 * 3 * 2 * 1 * 1
5 * 4 * 3 * 2 * 1
5 * 4 * 3 * 2
5 * 4 * 6
5 * 24
120


'''