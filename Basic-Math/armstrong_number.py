#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        
        num = n
        
        power = len(str(num))
        total = 0
        
        while num > 0:
            
            digit = num % 10
            
            total = total + digit ** power
            
            num = num // 10
            
        return total == n