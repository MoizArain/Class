# create a class employee with name,age,CNIC NO,contact
# create four different objects
# check the employee is greater than 30 or not
class Employee:
    def __init__(self,name,age,CNIC_no,contact):
        self.name = name
        self.age = age
        self.CNIC_no = CNIC_no
        self.contact = contact

    def check_young(self):
        if self.age > 30:
            return f"{self.name} is not young"
        else:
            return f"{self.name} is young"
        
    def check_age(self):
        if self.age >= 20:
            return f"{self.name} is not able to join"
        else:
            return f"{self.name} is able to join"
        
dummies1 = int(input("enter your age: "))
dummies2 = int(input("enter your age: "))
dummies3 = int(input("enter your age: "))
dummies4 = int(input("enter your age: "))

e1 = Employee("John",dummies1,"4130464730175", "0123456789")
e2 = Employee("Mary", dummies2,"3130464730174", "1233456789")
e3 = Employee("Smith", dummies3, "2130464730173", "2343456789")
e4 = Employee("Carlos", dummies4, "1130464730172", "3453456789")

print(" ")
print(e2.check_young())
print(e2.check_age())