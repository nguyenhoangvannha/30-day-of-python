import datetime

class MessageUser():
	user_details = []
	messages = []
	base_massage = """Hi %s! 
		Thank you for the purchase on %s. 
		We hope you are exicted about using it. Just as a
		reminder the purcase total was $%0.2f.
		Have a great one!
		Team CFE
		""" #%(names[i], today, amounts[i])
	def add_user(self, name ,amount):
		name = name[0].upper() + name[1:].lower()
		detail = {
			"name": name,
			"amount": amount
		}
		today = datetime.date.today()
		detail['date'] = today
		self.user_details.append(detail)
	def get_details(self):
		return self.user_details
	def make_message(self):
		for detail in self.get_details():
			name = detail['name']
			amount = detail['amount']
			today = detail['date']
			message = self.base_massage %(name, today, amount)
			print(message)
list_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
list_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

obj = MessageUser()
i = 0
while i < len(list_names):
	obj.add_user(list_names[i], list_amounts[i])
	i += 1
obj.make_message()
