# Base class
class Superhero:
    def __init__(self, name, power, hometown):
        self.name = name
        self.power = power
        self.hometown = hometown
        self.health = 100  # Default health value for all superheroes

    def introduce(self):
        return f"I am {self.name} from {self.hometown}, and my superpower is {self.power}!"

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} is defeated!"
        return f"{self.name} now has {self.health} health."

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        return f"{self.name} is healed and now has {self.health} health."


# Derived class
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, hometown, flight_speed):
        super().__init__(name, power, hometown)
        self.flight_speed = flight_speed  # Additional attribute for flying superheroes

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"

    # Polymorphism: Overriding the introduce method
    def introduce(self):
        return f"I am {self.name}, and I can fly! My superpower is {self.power}."


# Example usage
if __name__ == "__main__":
    hero1 = Superhero("Shadow", "Invisibility", "Gotham")
    hero2 = FlyingSuperhero("Skyhawk", "Super Strength", "Metropolis", 500)

    print(hero1.introduce())
    print(hero1.take_damage(30))
    print(hero1.heal(20))
    
    print(hero2.introduce())
    print(hero2.fly())
    print(hero2.take_damage(120))

