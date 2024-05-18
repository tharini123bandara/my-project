# elephant.py
from animal import Animal

class Elephant(Animal):
    def speak(self):
        return f"{self.name} says Trumpet!"
