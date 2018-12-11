#Methods vs class methods vs static methods

class Employee:

	raise_amount = 1.04
	num_of_employees = 0
	
	def __init__(self, first, last, pay): #Constructor
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		
		Employee.num_of_employees += 1
		
	def fullname(self): #Method
		return '{} {}'.format(self.first,self.last)
		
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount
		
emp_1 = Employee('Corey','Schafer',50000) 
emp_2 = Employee('Test','User',60000)

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
		
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)















