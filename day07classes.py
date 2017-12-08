class Animal():
	noise = "Gru gru"
	size = "Super small"
	color = "Brown"
	hair = "Covers body"
	def get_color(self):
		return self.color
	def make_noise(self):
		return self.noise
class Dog(Animal):
	name = "Hi"
	color = "Yellow"
	def get_color(self):
		print(self.name)
		return self.color

print(Dog().get_color())

dog = Dog()
dog.name = "Three"
print(dog.get_color())

instance = Animal()
print(instance.make_noise())
