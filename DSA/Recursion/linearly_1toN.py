class Solution: 
    
    
    def printNos(self,n, i = 1):
        #Code here
        
        if i > n:
            return
            
        print(i, end = " ")
            
        self.printNos(n, i + 1)
    