a = int(input("enter three subjects marks by user\n"))
b = int(input("enter three subjects marks by user\n"))
c = int(input("enter three subjects marks by user\n"))

total = a+b+c
percentage = (total*100)/300
print(percentage)
if(percentage>40):
    print("promoted to next class")
else:
    print("failed")