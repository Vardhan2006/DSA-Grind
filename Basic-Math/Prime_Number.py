class Solution:
    def isPrime(self, n):
        # code here
        
        if n < 2:
            return False
        else:
            
            is_prime = True
            
            for i in range(2, int(n**0.5) + 1):
                
                if n % i == 0:
                    is_prime = False
                    break
            
        if is_prime:
            return True
        else:
            return False
        
        self.isprime()

#Revised Once       