# main.py

from bird import Bird
from fish import Fish

def main():
   
    bird = Bird("Tweety")
    fish = Fish("Nemo")

    
    print(bird.speak())
    print(fish.speak())

if __name__ == "__main__":
    main()
