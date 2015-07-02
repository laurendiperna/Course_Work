#ex42
#This is useful:
#http://stackoverflow.com/questions/6396452/python-derived-class-and-base-class-attributes

## the class Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
        def __init__(self, thing, fur_length, legs):
            self.thing = thing
            self.fur_length = fur_length
            self.legs =legs
            
        def number_of_legs(self):
            amount = int(self.legs)
            print amount
            
        def how_hairy(self):
            self.hairy = 10 * int(self.legs)
            print self.hairy
        def printer(self):
            print "serisously!"
        
	
## is-a
class Dog(Animal):

	def __init__(self, name):
		##has-a
		self.name = name
		
	def wet_dog_strength(self):
		print "it just rained, what do you thin?"

		
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
	
    def __init__(self, fins, color):
        self.fins = fins
        self.color = color
	
##is-a
class Salmon(Fish):
    
    def __init__(self, wings, hue):
        self.wings = wings
        self.hue = hue
        
    def number_fins(self):
        self.num_wings = wings * 2
	
## is-a
class Halibut(Fish):
    def __init__(self,eyes):
        self.eyes = eyes
	
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
flipper  = Fish(2, 'red')

## has-a
crouse = Salmon(3, 'red')

## has-a
harry = Halibut('turquoise')
#to get this 'print harry.eyes' because harry is set to an instance of the Class Halibut where eyes is equal to turquoise
#Animal('dog', 2, 4) => <__main__.Animal at 0x105061490>
#dog = Animal('dog', 2, 4) => doesn't produce an error
#dog.legs => 4
#dog.number_of_legs => <bound method Animal.number_of_legs of <__main__.Animal object at 0x105d54790>>
#dog.number_of_legs() => 4
#dog.how_hairy() => 40

#so initialize by setting dog to Animal with three parameters, then call either the functions that take the parameters
#initialized in Animal using 'function()' or get the attribute with the '.' like dog.attribute no ()

#doggy = Dog(Animal) doesn't produce an error
#doggy => <__main__.Dog at 0x105d54990>

#if you set x  = to a class that inherits properties from another class you can call the parent class with c
#for example c = Elephants(), but Animals is a class, and you create Elephants like class Elephants(Animals)
#then you can call a function from Animals using c.Animal_function
#http://stackoverflow.com/questions/8853966/inheritance-of-attributes-in-python-using-init