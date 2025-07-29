class Dog:
    def make_sound(self):
        return "woof"
    
class Cat:
    def make_sound(self):
        return "meow"

class Cow:
    def make_sound(self):
        return "Moo"
    
def animal_sounds(vilangu):
    print(vilangu.make_sound())


dog = Dog()
cat = Cat()
cow = Cow()

animal_sounds(dog)
animal_sounds(cow)
animal_sounds(cat)
