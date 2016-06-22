## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog a class, has-a reference to class Animal and it has a name
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Cat a class, has-a reference to class Animal and it has a name
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Person is-a class, it has a name and a pet.
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person with name and salary
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish, reference to class Fish
class Salmon(Fish):
    pass

## Halibut is-a fish, reference to Fish.
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## frank is-a employee, with name Frank and salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet called rover.
frank.pet = rover

## flipper is-a Fish - it is an object of class Fish
flipper = Fish()

## crouse is a Salmon - it is an object of class Salmon
crouse = Salmon()

## harry is-a Halibut - it is an object of class Halibut.
harry = Halibut()
