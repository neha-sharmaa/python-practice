a, b, i= 1, 1, 0
n =int(input("Enter the value of n>>"))
c = a + b
print("the series is:")
print("%d %d %d" % (a, b, c), end="")
while(i < n-3):
    a = b
    b = c
    c = a + b
    print("%d" %c, end="")
    i = i + 1