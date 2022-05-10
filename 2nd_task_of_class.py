# create a class employee with name,age,CNIC NO,contact
# create four different objects
# check the employee is greater than 30 or not
class Employee:
    def __init__(self,name,age,CNIC_no,contact):
        self.name = name
        self.age = age
        self.CNIC_no = CNIC_no
        self.contact = contact
p1 = Employee("John",45,"4130464730175", "0123456789")
p2 = Employee("Mary", 32,"3130464730174", "0123456789")
p3 = Employee("Smith", 40, "2130464730173", "0123456789")
p4 = Employee("Carlos", 50, "1130464730172", "0123456789")
if p1.age > p2.age & p1.age > p3.age & p1.age > p4.age:
    print("p1 is greater than p2")
if p2.age > p1.age & p2.age > p3.age & p2.age > p4.age:
    print("p2 is greater than p1")
if p3.age > p1.age & p3.age > p2.age & p3.age > p4.age:
    print("p3 is greater than p1")
else:
    print("p4 is greater than p1,p2 and p3")