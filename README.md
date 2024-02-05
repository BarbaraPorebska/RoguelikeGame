# RoguelikeGame
"La Speluna", a company from San Escobar contacted us and asked
about creating aroguelike game for them. They didn't tell us much about
their needs, just a fewdetails about the framework of the game. They are big
fans of old-fashioned RPGgames from the days when graphics didn't matter that much,
and the mostimportant things were gameplay and a story.
The game should be about a creature (human? alien? ant? hacker?)
travellingthrough a dangerous and wild world (forest? planet? table?
meetups?). In thebeginning, the creature is weak and fragile, but
through the game they be level up,get tougher, collect powerful items,
and finally become able to defeat the final boss.Of course, the way to
the final boss is not a bed of roses: there are lots of obstacles(rivers?
craters? drops of milk? firewalls?) and many dangerous enemies.
Use yourimagination!

<br><b>Implement a basic board generator function to return a rectangular board of the given size.</br></b>
1. The
engine.create_board
function returns an empty, rectangular board as a list of lists of the given size. The board contains charactersaccording to the field type (such as spaces all around and wall icons on its edges).
2. The game has at least 3 boards/levels with diff erent inhabitants.
3. Gates are added on the edges (one gate character instead of one piece of wall).


<br><b>Implement board and player display. The player always sees the current board only.</br></b>
1. The function
ui.display_board
displays a board (passed as an argument).
2. The function
engine.put_player_on_board
places the player icon on the board.


<br><b>Implement player movement on the board using the WASD keys.</br></b>
1. The WASD keys move the player up, left , down, and right on the screen, respectively.
2. The player cannot move through walls.
3. Going through a gate loads another board (the same door always leads to the same place).


<br><b>Implement items that can be added to the player inventory by moving over them.</br></b>
1. The items have at least two attributes, name and type. You can add others as well.
2. The items are displayed on the board.
3. The items disappear from the board when the player moves over them. The items do not reappear when the player reenters the board.
4. One type of items is food – these update the player state and disappear.
5. Other types of items are added to the player inventory when picked up.
6. Implement at least two features connecting to items (such as keys for opening gates, weapons, armors, and so on).
7. The inventory is displayed upon pressing the
I
key.

 
<br><b>The player has various (constant and variable) attributes.</br></b>
1. The player character has a name, a race (such as elf or dwarf), and health. You can add others as well.
2. The player can choose or configure their character before starting the game.
3. The player character can die if its vital attributes become too low.
4. The character's main attributes are always displayed on the screen.


<br><b>Implement other inhabitants around the player character.</br></b>
1. Other characters have three mandatory attributes: name, type, and health.
2. Create at least three diff erent types (in addition to the player and the boss).
3. The characters move autonomously, and do not go through the walls. The characters move only when the player moves.
4. Implement a creature that says something upon meeting the player.
5. Fight is implemented against enemies. A fight consist of rounds (hits). A hit happens when the player tries to move over the enemy. Hits on thehealth of the player and the creature are calculated based on their attributes, the inventory, and randomness.


<br><b>A roguelike game needs a boss fight at the very end.</br></b>
1. The boss is a larger (at least 5-by-5), autonomously moving character.
2. An extremely hard boss fight is implemented (for example, special weapons are needed, or the hit chance is low).
3. There is a secret code that makes finishing the game easier.

