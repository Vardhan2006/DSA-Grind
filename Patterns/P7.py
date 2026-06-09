n = 5

for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    for j in range(n-i-1):
        print(" ", end=" ")
               
    print()


'''

        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 

'''

#step 1 we need to print the (space, star, space)
# [space, star, space]
# [4, 1, 4]
# [3, 3, 3]
# [2, 5, 2]
# [1, 7, 1]
# [0, 9, 0]

# step 2 figure out the formula for space n - i - 1 
# step 3 figure out the formular for star 2*i + 1
# step 4 use the same space logic on right also

# Revised Once