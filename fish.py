# fish.py
from animal import Animal

class Fish(Animal):
    def speak(self):
        return f"{self.name} says Blub!"
