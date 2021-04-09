'''def greet(name):
    print ("Good day" + name)

name = input("enter the name of the person:\n")
greet(str(name)) 
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(4)
print(f)