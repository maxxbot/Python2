#Python Object-Oriented Programming

class Employee:
	
	def __init__(self, first, last, pay): #Constructor
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		
	def fullname(self): #Method
		return '{} {}'.format(self.first,self.last)

emp_1 = Employee('Corey','Schafer',50000) #Instance passed automatically
emp_2 = Employee('Test','User',60000)

print(emp_1)
print(emp_2)


print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())

#Same result but one must be passed instance

print(emp_2.fullname())
print(Employee.fullname(emp_2))



















