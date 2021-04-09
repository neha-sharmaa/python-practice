flag = 1
n = int(input("enter the no. n>> "))
if(n <= 1):
    print("factorial is 1")
    exit(0)
else:
    while(n > 1):
        flag = flag * n
        n = n-1
        print("%d\n" % flag, end ="")

'''n = int(input("enter any no.\n"))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
    print({factorial})'''
