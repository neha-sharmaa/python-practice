class Employee:
    company = "Google"
    
    def __init__(self,name,salary,company):
        self.name = name
        self.salary = salary
        self.company = company      
        print(f"Ms. {self.name} Welcome to our company {self.company} on {self.salary} permonth package")

    def detailSalary(self, signature):
        print(f"{signature} welcome back")
    
    def printSalary(self):
        print(f"Hi harry you got selected for {self.company} andd your package is{self.salary} k")

    @staticmethod
    def empTime():
        print("working hour are 9am to 5pm")

harry = Employee("Rahul",10000,"youtube")
'''harry.name = "Rahul"
harry.company = "youtube"
harry.salary = 10000'''
harry.detailSalary("thanks")
harry.printSalary()
harry.empTime(),