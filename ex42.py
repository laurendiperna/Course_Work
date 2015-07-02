#ex42
#This is useful:
#http://stackoverflow.com/questions/6396452/python-derived-class-and-base-class-attributes

## the class Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
	def __init__(self, type,fur_length, legs):
		self.type = type
		self.fur_length = fur_length
		self.legs = legs
	
	def number_of_legs(self):
		amount = int(self.legs)
		print amount
	
	def how_hairy(self):
		return 10 * int(self.fur_length)
	
## is-a
class Dog(Animal):

	def __init__(self, name):
		##has-a
		self.name = name
		
	def wet_dog_strength(self):
		wetness = Animal.how_hairy()
		return wetness
		
## is-a
class Cat(Animal):
	
	def __init__(self, name):
		##has-a
		self.name = name
		
## is-a
class Person(object):

	def __init__(self, name):
		##has-a
		self.name = name
		
		##Person has-a pet of some kind
		self.pet = None
		
## is-a
class Employee(Person):
	
	def __init__(self, name, salary):
	
		##From the function named super with the Employee and self parameters,
		# get the __init__ and call it with the name parameter
		super(Employee, self).__init__(name)
		
		##From self get the salary attribute and set to salary
		self.salary = salary
## is-a
class Fish(object):
	pass
	
##is-a
class Salmon(Fish):
	pass
	
## is-a
class Halibut(Fish):
	pass
	
##has-a, but Dog("Rover") is-a
rover = Dog("Rover")

##has-a
satan = Cat("Satan")

##has-a
mary = Person("Mary")

## has-a
mary.pet = satan

## has-a
frank = Employee("Frank", 120000)

##has-a
frank.pet = rover

## has-a
flipper  = Fish()

## has-a
crouse = Salmon()

## has-a
harry = Halibut()