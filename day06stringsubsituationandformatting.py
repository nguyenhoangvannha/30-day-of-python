text = "This is a {var} string".format(var = "really cool")
print(text)
my_name = "Nha"
name = "My name is {the_name}\n\tOk hi: {the_name}.".format(the_name = my_name)
print(name)
text = "This is a argument {0} in {1}".format("zero", 2017)
print(text)
text = "I am %s and I'm %d years old" %(my_name, 20)
print(text)

import datetime
today = datetime.date.today()
print(today)
text = '{today.month}/{today.day}/{today.year}'.format(today = today)
print(text)

now = datetime.datetime.utcnow()
text = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(now)
print(text)