'''
def f():
    print(1)

    f()        # infinite recursion

f() 
'''


# def f():
#     print(1)  this is a recusrion loop calls function print 1 then calls functions repeats

#     f()


def f(count):
    print(count)

    if count == 4:
        return
    f(count + 1)
f(0) 