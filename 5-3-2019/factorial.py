
def get_input_user():
	user_input = int(input("Enter the number:"))
	return user_input	

def find_factorial(user):
	if user == 0:
		return 1
	else:
		return(user * find_factorial(user-1))
		
def main():
	try:
		user = get_input_user()
		fact = find_factorial(user)
		print("Factorial Number",user,"is",fact)
	except (SyntaxError, ValueError):		
		print("You didn't enter a number")		

if __name__ == '__main__':
  main()