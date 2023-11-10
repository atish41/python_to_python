#parametarized constructor and instance method

class Employee:
	def __init__(self,number):
		self.number=number
	def show(self):
		print("Employee id :",self.number)

e1=Employee(4)
e2=Employee(5)
e3=Employee(6)
e1.show()
e2.show()
e3.show()