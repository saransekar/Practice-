class Student:
	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

	def get_subject_marks(self,maths,phyics,biology):
		self.maths = maths
		self.phyics = phyics
		self.biology = biology

	def display_totalmarks(self):
		return("Total Marks: {} ".format(self.maths + self.phyics + self.biology)) 		
				
def create_students():
	name = input("Enter the your name: ")
	age = int(input("Enter the your age: "))
	gender = input("Enter the gender: ")
	student = Student(name,age,gender)
	return student

def create_subjects():
	maths = int(input("Enter the maths subject mark: "))
	phyics = int(input("Enter the phyics subject mark: "))	
	biology = int(input("Enter the biology subject mark: "))
	return maths,phyics,biology

if __name__ == '__main__':	
	students = create_students()
	print("student name:",students.name)
	print("student age:",students.age)
	print("student gender:",students.gender)
	maths,phyics,biology = create_subjects()
	students.get_subject_marks(maths,phyics,biology)
	print(students.display_totalmarks())





class Employee:  
    def __init__(self,name):  
        self.name = name;  
        #self.id = id; 
        
    def display_employee_name(self,choice): 
    	self.choice = choice
    	if self.name == self.choice:
    		print("Employee name",self.name)
    	else:
    		print("Niooo")	
       

def create_employees():         
	name = input("Enter the your name: ")
	#id = int(input("Enter the your id: "))
	emp = Employee(name)  
	#print(getattr(emp,'name'))
	#print(getattr(emp,'id'))
	return emp
 
if __name__ == '__main__':
	while True:
		option = int(input("Enter Option:"))
		if option == 1:	  
			employee = create_employees()
			print(employee.name)
		
		if option == 2:
			choice = input("Enter choice:")
			employee.display_employee_name(choice)
			#print(employee)










class AttrDict(dict):
    def __getattr__(self, item):
        return self[item]

attrd = AttrDict()
attrd["key"] = "value"
print(attrd.key)        