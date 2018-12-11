#Property Decorator

class Employee:

	raise_amount = 1.04
	num_of_employees = 0
	
	def __init__(self, first, last, pay): 
		self.first = first
		self.last = last
		self.pay = pay
	
	@property
	def email(self): 
		return '{}.{}'.format(self.first,self.last)
	
	@property	
	def fullname(self): 
		return '{} {}'.format(self.first,self.last)
		
	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last
		
	@fullname.deleter
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None
		

emp_1 = Employee('Corey','Schafer',50000) 

emp_1.fullname = 'Jeb! Bush'	

print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)









