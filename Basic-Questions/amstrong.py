num = int(input('enter a number: '))

#we copy the original and while the original is safe and this n changes while in the loop
n = num

# Taking the len to add it as power to the original digits
power = len(str(num))
total = 0

while n > 0:

    #Taking the last digit
    digit = n % 10

    # Adding the power to the number and calculating
    total = total + digit ** power

    #Remove the last digit
    n = n // 10

if total == num:
    print('Amstrong Number')
else:
    print('Not Amstrong Number')