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
print(p1.name)
print(p2.age)
print(p3.CNIC_no)
print(p4.contact)
