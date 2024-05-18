# bird.py
from animal import Animal

class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"
