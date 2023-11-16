#instance variable
class Student:
	def __init__(self,name,number):
		self.name=name
		self.number=number

s1=Student('daniel',101)
s2=Student('Prasad',102)

print("Studetn info :")
print("Name :",s1.name)
print("id :",s1.number)


print("student info:")
print("Name:",s2.name)
print("id:",s2.number)


