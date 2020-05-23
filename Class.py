class Employee:
	empCount = 0

	def __int__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	@staticmethod
	def displayCount():
		print("\n Total Employee %d", Employee.empCount)

	def displayEmployee(self):
		print("\n Name:", self.name, ",Salary:", self.salary);



emp1 = Employee("ABC",2000)
emp2 = Employee("XYZ",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("\n Total Employee: ", Employee.empCount)
