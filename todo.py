class ToDo:

	def __init__(self,task):
		self.task = task
		self.is_complete = False 

	def update_task(self):
		self.is_complete = True