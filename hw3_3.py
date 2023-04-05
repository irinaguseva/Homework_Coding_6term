from time import sleep

class Cat:
    def __init__(self, name, age, health, stamina, level):
        self.name = name
        self.age = age
        self.health = health
        self.stamina = stamina
        self.level = level
        
    def __str__(self):
        return f'The name of the cat is {self.name} and it is {self.age} years old.'
    
    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age}, health={self.health}, stamina={self.stamina}, level={self.level})'
    
    def speak(self):
        print('Meow!')
    
    def sleep(self):
        print('Z-z-z..')
        sleep(1)
        self.stamina = 10
    
    def feed(self):
        print('Mrrrthanks!')
        self.health = 10
    
    def play(self):
        print('Let\'s play!')
        self.level += 1
    
    def _grow(self):
        self.age += 1
        if self.age > 18:
            print(f'{self.name} has passed out :(')
        else:
            print(f'{self.name} has got older!')
            