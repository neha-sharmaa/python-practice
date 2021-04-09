text = input("enter the text by user:\n")
if("make a friend" in text):
    spam = True
elif("hello world" in text):
    spam = True
else:
    spam = False


if(spam):
    print("This is spam text")
else:
    print("This is not spam text")