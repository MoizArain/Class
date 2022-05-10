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
            return "not young"
        else:
            return "still young"

e1 = Employee("John",45,"4130464730175", "0123456789")
e2 = Employee("Mary", 32,"3130464730174", "1233456789")
e3 = Employee("Smith", 40, "2130464730173", "2343456789")
e4 = Employee("Carlos", 50, "1130464730172", "3453456789")

print(e2.check_young())