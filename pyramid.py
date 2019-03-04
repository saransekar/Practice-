import argparse
def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", metavar = 'symbol', nargs = '?', help = "enter the symbol")
	parser.add_argument("-l", type = int, metavar='limit', nargs='?', help = "enter the number")
	parser.add_argument("-d", choices = ['left', 'right', 'downside', 'upside'], metavar ='direction', nargs = '?', help = "enter the word")
	args = parser.parse_args()
	return args

def instruct_pyramid():	
	print("Please select any one below given input:\n1.left triangle pyramid\n2.right triangle pyramid ")
	print("3.downside up triangle pyramid\n4.upside down triangle\n5.Exit")

def get_input_user():
	user_input = int(input("Enter the number:"))
	return user_input	

def form_left_triangle_pyramid(limit,i):
	if limit == 0:
		return 0
	else:
		print('' * ( limit + 1 ) + symbol * ( i * 2 + 1 ))
		return form_left_triangle_pyramid( limit - 1, i + 1 )

def form_right_triangle_pyramid(limit,i):
	if limit == 0:
		return 0
	else:
		print(' ' *( 2*limit - 2) + symbol * (i + 1))
		return form_right_triangle_pyramid( limit - 1, i + 2 )

def form_downside_up_pyramid(limit,i):	
	if limit == 0:
		return 0
	else:
		print(' ' * ( limit + 1 ) + symbol * ( i * 2 + 1 ))
		return form_downside_up_pyramid( limit - 1, i + 1 )

def form_upside_down_pyramid(limit,i):
	if limit == 0:
		return 0
	else:
		print(' ' * ( i + 1 ) + symbol * ( limit * 2 - 1 ))
		return form_upside_down_pyramid( limit - 1, i + 1 )

def main():
	global symbol,limit
	args_input = create_parser()
	symbol = args_input.s
	limit = args_input.l
	word = args_input.d
	user = 0
	i = 0
	if word is None:
		instruct_pyramid()
		user = get_input_user()
	if word == 'left' or user == 1:
		form_left_triangle_pyramid(limit,i)
	elif word == 'right' or user == 2:
		form_right_triangle_pyramid(limit,i)
	elif word == 'downside' or user == 3:
		form_downside_up_pyramid(limit,i)
	elif word == 'upside' or user == 4:
		form_upside_down_pyramid(limit,i)
	else:
		print("Inavalid")				
if __name__ == '__main__':
  main()
