#Class variables


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
		
emp_1 = Employee('Corey','Schafer',50000) 
emp_2 = Employee('Test','User',60000)


#Wont show raise_amount
print(emp_1.__dict__)

#Will show raise_amount
print(Employee.__dict__)

emp_1.raise_amount = 1.05


print(emp_1.pay)

print(Employee.num_of_employees)






