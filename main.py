import todo

def instruct_todo_task():
	print("Please select any one below given:\n1.Create ToDo\n2.List ToDo\n3.Update ToDo")

def create_todo():
	task = input("Enter the your task:")
	if task != '':
		task = todo.ToDo(task)
		return task	
	else:
		print("Please enter your task")
		
def display_todo_list(todolist):	
	for todo_idx, todo_val in enumerate(todolist):
		#print("{}{}{}{}".format(todo_idx + 1,".",todo_val.task,"- Completed",todo_val.is_complete))
		print("{}{}{}".format(todo_idx + 1,".",todo_val.task))


def main():
	todolist = []
	updatedlist = []	
	while True:
		instruct_todo_task()		
		option = int(input("Enter Option:"))
		if option == 1:
			todo_task = create_todo()
			if todo_task is None:
				todolist = []
			else:
				todolist.append(todo_task)	
			
		elif option == 2:
			if todolist != []:
				display_todo_list(todolist)
			else:
				print("Please create todo task")
						
		elif option == 3:				
			if todolist != []:
				choice = int(input("Enter the number:"))
				if choice <= len(todolist):			
					todo = todolist[choice-1]					
					if todo.is_complete:
						print("Already Completed")
					else:	
						todo.update_task()
						updatedlist.append(todo)			
						for updatedlist_idx, updatedlist_val in enumerate(updatedlist):
							print("{}{}{}{}".format(updatedlist_idx + 1,".",updatedlist_val.task,"- Completed",updatedlist_val.is_complete))
				else:
					print("Correct choice input")
			else:
				print("Please create todo task")

		elif option == 4:
			exit()

		else:
			print("Doesn't exist")		
			 
if __name__ == '__main__':
	try:
		main()
	except (SyntaxError, ValueError):		
		print("You didn't enter a number")				