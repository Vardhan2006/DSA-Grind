#approach 1

n = 5
for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        print(i, end= " ")
    print()


#approach 2
'''
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(j + 1, end= " ")
    print()
'''


'''

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

'''

# step 1 we have to start from n then reduce it by 1 on each loop which means 1, n + 1 this is outer loop runs till 1 to 5 
# now we have to print 1 5 times 2 4 times so we will basically print (n - 1) times which is inner loop
# now we just have to pirnt j + 1 to get the pattern