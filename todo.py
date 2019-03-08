class ToDo:

	def __init__(self,task):
		self.task = task

	def update_task(self,choice,todolist):
		self.choice = choice
		if self.choice == len(todolist):
			print("correct")
		else:
			print("wrong")	

			
		


