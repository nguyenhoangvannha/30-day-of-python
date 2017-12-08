from py_day_mod.make_message import MessageUser

list_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
list_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

obj = MessageUser()
i = 0
while i < len(list_names):
	obj.add_user(list_names[i], list_amounts[i])
	i += 1
obj.make_message()