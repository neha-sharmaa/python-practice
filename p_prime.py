num  = int(input("enter any no.\n"))
prime = True
for i in range (2,num):
    if (num%i == 0):
        prime = False
        break
if prime:
    print("this is prime no.")
else:
    print("this is non prime no.")