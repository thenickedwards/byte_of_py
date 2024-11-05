# Parent Class or Superclass
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def walk(self, direction, speed):
        print(f'{self.name} walks {direction} at {speed}')
        
    def talk(self, speech):
        print(f'{self.name} says, "{speech}"')

# Child Class or Subclass
# inherits 'Human' class attributes
# 
class Wizard(Human):
    def __init__(self, name, age, spell_slots):     # by itself this will overwrite the parent class
        super().__init__()                          # the super() method can be used to call the parent class __init__
        self.spell_slots = spell_slots              # this attribute will be specific to wizards
        
    def cast_spell(self, spell):
        print(f'{self.name} has cast {spell}')