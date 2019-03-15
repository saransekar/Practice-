import contact

def instruct_contact():
	print("Please select any one below given:\n1.Create\n2.Update\n3.Delete")

def create_contact():
	user_name = input("Enter the name:")
	mobile = int(input("Enter the mobile number:"))
	new_contact = contact.Contact(user_name,mobile)
	return new_contact

def display_contact_list(user_contactlist):
		for user_idx, user_val in enumerate(user_contactlist):
			print("{}{}{}".format(user_idx + 1,".",user_val))
		
def main():
	user_contactlist = []
	mobile_contactlist = []
	while True:
		instruct_contact()
		option = int(input("Enter Option:"))
		if option == 1:
			contact = create_contact()			
			user_contactlist.append(contact.name)
			mobile_contactlist.append(contact.mobile)

		if option == 2:
			display_contact_list(user_contactlist)
			choice = int(input("Enter the number:"))
			contact_num = int(input("Enter the new number:"))
			new_contact_num = contact.update_contact(contact_num)
			for mobile_idx, mobile_val in enumerate(mobile_contactlist):
				if mobile_idx == choice-1:
					mobile_contactlist[mobile_idx] = new_contact_num	
			print("updated contact number - ",mobile_contactlist)		
		
		if option == 3:
			display_contact_list(user_contactlist)
			contact_list = int(input("Enter the number:"))
			del_contact = contact.delete_contact(contact_list)
			for mobile_idx, mobile_val in enumerate(mobile_contactlist):
				if mobile_idx == del_contact-1:
					del mobile_contactlist[mobile_idx]
					del user_contactlist[mobile_idx]
			print("Delete contact username {} and mobile number{}".format(mobile_contactlist,user_contactlist))								

		if option == 4:
			exit()

if __name__ == '__main__':						
	main()