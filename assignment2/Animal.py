from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Mammals(Animal):
    def sound(self):
        return "Varies by species"

    def move(self):
        return "Walk or run on limbs"

    def eat(self):
        return "Mostly plants or other animals"

class Reptiles(Animal):
    def sound(self):
        return "Hiss or silent"

    def move(self):
        return "Crawl or slither"

    def eat(self):
        return "Carnivorous—eat insects, rodents, etc."
    
class Birds(Animal):
    def sound(self):
        return "Chirp or sing"

    def move(self):
        return "Fly using wings"

    def eat(self):
        return "Seeds, insects, worms"

class Amphibians(Animal):
    def sound(self):
        return "Croak or ribbit"

    def move(self):
        return "Hop or swim"

    def eat(self):
        return "Insects, larvae, and small aquatic creatures"


def show_animal_behavior(animal_obj, animal_type):
    print(f"{animal_type} Behavior:")
    print("Sound:", animal_obj.sound())
    print("Move :", animal_obj.move())
    print("Eat  :", animal_obj.eat())
    print()

show_animal_behavior(Mammals(), "Mammals")
show_animal_behavior(Reptiles(), "Reptiles")
show_animal_behavior(Birds(), "Birds")
show_animal_behavior(Amphibians(), "Amphibians")
