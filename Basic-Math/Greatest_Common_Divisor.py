# Euclidean ALgorithm for optimized version


# according to Euclidean Algo gcd(n1,n2) = gcd(n1-n2, n2) = gcd(a%b, b)


class Solution:
    def gcd(self, a, b):
        # code here
        
        while a > 0 and b > 0:
            
            if a > b:
                a = a % b       #Time Complexity is O(log phi min(a,b)) because when ever divison happen no of iterations will be in logarthemic 
            else:
                b = b % a
                
        if a == 0:
            return b
        else:
            return a
                