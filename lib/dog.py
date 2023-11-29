#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed="Mutt"):
        if not (isinstance(name, str) and 1 <= len(name) <= 25):
            print("Name must be a string between 1 and 25 characters.")
            return
        if breed not in ["Pug", "Labrador", "Dalmatian"]:
            print("Breed must be in the list of approved breeds.")
            return

        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

    pass
