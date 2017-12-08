list_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
list_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]
import datetime

def make_massages(names, amounts):
	i = 0
	while i < len(names):
		today = datetime.datetime.now()
		message = """Hi %s! 
		Thank you for the purchase on %s. 
		We hope you are exicted about using it. Just as a
		reminder the purcase total was $%0.2f.
		Have a great one!
		Team CFE
		""" %(names[i], today, amounts[i])
		print(message)
		i += 1
make_massages(list_names, list_amounts)