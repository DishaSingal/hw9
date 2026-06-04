from abc import ABC, abstractmethod

class Instrument:
    def __init__(self, name):
        self.name = name 

    def play_sound(self):
         pass

    def display(self):
            print(f"Name: {self.name}")

class Guitar(Instrument):
     
     def __init__(self, name):
          super().__init__(name)

     def play_sound (self):
          print(f"{self.name} make the sound strum! strum!")

class Drum(Instrument):
     def __init__(self,name):
          super().__init__(name)

     def play_sound (self):
          print(f"{self.name} makes the sound Boom! Boom!")

instrument_1 = Guitar("Acoustic Guitar")
instrument_2 = Drum("Bass drum")

for x in (instrument_1,instrument_2)
x.play_sound()

print()


