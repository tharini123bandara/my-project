# main.py

from bird import Bird
from fish import Fish
from elephant import Elephant

def main():
   
    bird = Bird("Tweety")
    fish = Fish("Nemo")
    elephant = Elephant("Dumbo")
     
    
    print(bird.speak())
    print(fish.speak())
    print(elephant.speak())


if __name__ == "__main__":
    main()
