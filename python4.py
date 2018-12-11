#Creating Subclasses

from python3 import Employee


class Developer(Employee):
	raise_amount = 1.10
	
	def __init__(self, first, last, pay, prog_lang): 
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang
		
class Manager(Employee):
	
	def __init__(self, first, last, pay, employees = None): 
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
			
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
			
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
			
	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())
	

dev_1 = Developer('Corey','Schafer',50000, 'Python') 
dev_2 = Developer('Test','User',60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# ~ print(mgr_1.email)

# ~ mgr_1.add_emp(dev_2)
# ~ mgr_1.print_emps()
# ~ mgr_1.remove_emp(dev_1)
# ~ mgr_1.print_emps()


# ~ print(dev_1.email)
# ~ print(dev_2.email)

# ~ print(dev_1.pay)
# ~ dev_1.apply_raise()
# ~ print(dev_1.pay)

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))


















