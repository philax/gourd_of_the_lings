from character import *
from encounter import *

print "<Insert Sweet Splash Screen Here!!>"

player1 = Character(100, "Our Hero")
name = player1.name

# kick open another door, munchkin style!
#while thing
new_encounter = Encounter(player1)
new_encounter.battle()