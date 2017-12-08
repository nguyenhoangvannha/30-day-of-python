class Animal():
	name = "A Animal"
	noise = "Gru gru"
	size = "Super small"
	color = "Brown"
	hair = "Covers body"
	def get_color(self):
		return self.color
	@property
	def make_noise(self):
		return self.noise

dog = Animal()
print(dog.make_noise)

#kwarg = Keyword argument
def some_func(arg_1, arg_2, arg_3, kwarg_ = None):
	if kwarg_ != None :
		print(kwarg_)
	pass
some_func(0,0,0, "hello")