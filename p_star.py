'''n = int(input("enter the no. \n"))
for i in range(-1,n+1):
    print("*" * (i+2))'''

'''n = int(input("enter the no. \n"))  
  #n = 4
for i in range(0,n+1):# 1 to 5
        print("*" * (i+1))
        for j in range(1,n+1):# 1 to 4
            print("   " * (j+1))
'''

def fun_star(n):
  for i in range (n+1,1,-1):  
    print("*"*(i-1))

s = fun_star(6)
print (s)