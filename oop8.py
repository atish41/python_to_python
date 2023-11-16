#initializing instance variables inside constructor

class Employee:
	def __init__(self):
		self.eno=10
		self.ename="Daniel"
		self.esal=10000

Emp=Employee()

print("Employee number:",Emp.eno)
print("Employee name:",Emp.ename)
print("Employee salary:",Emp.esal)

