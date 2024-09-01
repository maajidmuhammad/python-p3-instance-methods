
#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
    def bark(self):
        print("Woof!")
    def sit(self):
        print("The dog is sitting.")
    pass

fido = Dog()
# <__main__.Dog object at 0x1027f07f0>
fido.bark()
fido.__dir__()
snoopy = Dog()
snoopy.bark()