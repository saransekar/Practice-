"""class ToDo:

	def __init__(self,task):
		self.task = task

	def update_task(self,updated,todolist):
		self.__updated = updated
		updated_task = False
		if self.__updated <= len(todolist):
			updated_task = True
			updated = todolist[self.__updated - 1]
			#print(updated.__task,"Completed")
			print(updated.task,"Completed")
		else:
			print("Incompleted")"""




class ToDo:

	def __init__(self,task):
		self.task = task
		self.is_complete = False 

	def update_task(self):
		self.is_complete = True