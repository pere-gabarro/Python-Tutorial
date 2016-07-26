# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

# Instanciem dos objectes
car1 = Vehicle()
car2 = Vehicle()

# Fixem els atributs del car1
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60.000

# Fixem els atributs del car1
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10.000

