""" import todo
todolist1 = []
def instruct_todo_task():
	print("Please select any one below given:\n1.Create ToDo\n2.List ToDo\n3.Update ToDo")

def create_todo():
	todo_input = input("Enter the your task:")
	todo_input = todo.ToDo(todo_input)
	return todo_input

def display_todo_list(todolist):
	for todo_val in todolist:
		print(todolist1.append(todo_val.todo))
	return(todolist1)

def update_todo(choice,todolist1):

	updated_todo = {}	
	initial = 0
	for i in range(1,len(todolist1)+1):	
		o = ''				
		updated_todo[i] = "%s%s" % (o, todolist1[initial])
		initial = initial + 1
	

	for update_idx,update_val in updated_todo.items():

		if choice == update_idx:
			print(update_val,"Completed")
 

if __name__ == '__main__':
	todolist = []	
	while True:
		instruct_todo_task()		
		option = int(input("Enter Option:"))
		if option == 1:
			todo_task = create_todo()
			todolist.append(todo_task)		
		if option == 2:
			todolist1 = display_todo_list(todolist)
			#print(todolist1)
		if option == 3:
			#for todo_idx,todo_val in enumerate(todolist):
				#print("{}{}{}".format(todo_idx + 1,".",todo_val.todo))

			choice = int(input("Enter choice:"))
			update_todo(choice,todolist1)	"""





import todo

def instruct_todo_task():
	print("Please select any one below given:\n1.Create ToDo\n2.List ToDo\n3.Update ToDo")

def create_todo():
	task = input("Enter the your task:")
	task = todo.ToDo(task)
	return task

def display_todo_list(todolist):
	for todo_val in todolist:
		print(todo_val.task)

 
if __name__ == '__main__':
	todolist = []	
	while True:
		instruct_todo_task()		
		option = int(input("Enter Option:"))
		if option == 1:
			todo_task = create_todo()
			todolist.append(todo_task)		
		if option == 2:
			display_todo_list(todolist)			
		if option == 3:
			choice = int(input("Enter choice:"))
			todo_task.update_task(choice,todolist)	
			print(todo_task.choice)