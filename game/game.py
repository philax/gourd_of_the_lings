from entity.character import *
from controller.encounter import *

print "<Insert Sweet Splash Screen Here!!>"

name = raw_input('Welcome.  What is your name? ')
player1 = Character(name, 100, 10)


# kick open another door, munchkin style!
#while thing
new_encounter = Encounter(player1)
new_encounter.battle()

# have view draw screen & draw input