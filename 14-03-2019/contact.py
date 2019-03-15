class Contact:

	def __init__(self, user_name, mobile):
		self.name = user_name
		self.mobile = mobile
	
	def update_contact(self,contact_num):
		self.num = contact_num
		return self.num	

	def delete_contact(self,contact_list):
		self.contact = contact_list
		return self.contact	
