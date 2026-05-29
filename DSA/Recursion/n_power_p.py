class Solution:
    def RecursivePower(self, n, p):
        # code here
        
        if p == 0:
            return 1
        
        return n * self.RecursivePower(n, p - 1)    

'''

2 * RecursivePower(2, 3)

2 * (2 * RecursivePower(2, 2))

2 * (2 * (2 * RecursivePower(2, 1)))

2 * (2 * (2 * (2 * RecursivePower(2, 0))))

2 * (2 * (2 * (2 * 1)))      ← Base case returns 1

Now backtracking starts:

2 * (2 * (2 * 2))

2 * (2 * 4)

2 * 8

16


'''