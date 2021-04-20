class calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"the square value of number is {self.num**2}")
    
    def square_root(self):
        print(f"the squareroot value of number is {self.num**0.05}")
       

square = calculator(4)
square.square()
square.square_root()