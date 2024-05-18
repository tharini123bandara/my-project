# main.py
from dog import Dog
from cat import Cat

def main():
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    print(dog.speak())
    print(cat.speak())

if __name__ == "__main__":
    main()