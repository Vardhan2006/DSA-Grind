n = 12341234
count = 0
        
while n > 0:
    digit = n % 10
    count = count + 1
    n = n // 10

print(count)