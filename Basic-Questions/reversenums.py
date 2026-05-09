'''
n = 12345
print (str(n)[::-1])
'''

'''
n = 12345
rev = 0

while n > 0:

    # Takes the last digit for example: 12345 % 10 = 5 which is the last digit
    digit = n % 10

    #now here we multiply it with 10 to create space then to add the number example: 543 = 54 * 10 + 3 
    rev = rev * 10 + digit

    #In here we remove the digit from the n which are already taken
    n = n // 10
print(rev)
'''

