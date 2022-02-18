class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise= noise
        self.energy = 50
        self.health = 100
        
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        print(f"Your pet's energy is now {self.energy}")
        self.health += 10
        print(f"Your pet's health is now {self.health}")
        return self

    # play() - increases the pet's health by 5
    def play (self):
        self.health += 5
        print(f"Your pet's health is {self.health}")
        self.energy -= 15
        print (f"Your pet's energy is {self.energy}")
        return self
    # noise() - prints out the pet's sound 
    def noise(self):
        print(self.noise)


class Ninja:
    def __init__( self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("lima", "terrier", "sit", "bark")

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe (self):
        self.pet.noise()
        return self

lima = Pet("lima", "terrier", "sit", "bark")
steph = Ninja("steph", "maguina", "cookies", "earthborne", lima)

steph.walk()
steph.feed()
steph.bathe()





