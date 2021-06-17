num = int(input("Enter how many number do you want for the sequence: "))

a = 0
b = 1

print(a)
print(b)

for i in range (0, num):

    c = a + b
    print(c)
    
    a = b
    b = c

    
