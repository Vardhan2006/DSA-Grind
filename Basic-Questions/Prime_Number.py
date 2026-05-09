
#taking input
n = 8

#if < 2 than it will not be prime

if n < 2:
    print('Not prime')
else:
    is_prime = True
    #checking till root of n becuase beyond it wont make sense
    for i in range(2, int(n**0.5) + 1):
        #than checking if 8 divisible from 2 to root of n if yes print false than break
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print('prime')
    else:
        print('not prime')

