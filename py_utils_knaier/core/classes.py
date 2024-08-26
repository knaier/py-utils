class Dog:
    """ This comment is DocString. This is a simple dog. Class names are in CamelCase """

    def __init__(self, name, age):
        # Instance variables should be lwercase with _ between words i.e. index_found
        self.name = name
        self.age = age
    
    def sit(self):
        """ Sit doggy """
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """ Rollover doggy """
        print(f"{self.name} rolled over")

    def __str__(self):
        return f"Dog called {self.name} whch is {self.age} years old"

class Grayhound(Dog):
    """ Grayhounds are a type of dog which are fast """

    def __init__(self, name, age):
        super().__init__(name, age)
    
    def sit(self):
        """ ROllover grayhound """
        print(f"Grayhounds dont like doesn this")
        super().sit()
