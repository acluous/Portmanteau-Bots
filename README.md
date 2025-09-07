This is a Python program and a Discord bot written with discord.py to build portmanteaus term by term.

# What is a Portmanteau?
Portmanteaus (also known as ports) are a puzzle type originating in Pokemon Showdown's Scavengers room.

An example of a port is 
\[Gen 1 Pokemon\] \[Bug-Type Pokemon\] \[Gen 3 Pokemon\] \[Starter Pokemon\] \[Rock-Type Pokemon\]

This port could have ClefabLedyBarboaChimchArcheops as a solution, consisting of the Pokemon Clefable, Ledyba, Barboach, Chimchar, and Archeops.

Each term/Pokemon in a port must satisfy the corresponding description. For example, Clefable is a Pokemon from Generation 1.

In addition, each term in a port must end with a substring which is the beginning of the next term in the port so that all of the terms can be chained together.

Substrings must be at least length two and cannot be identical to either term.

For example, Clefable Elgyem with a substring of "e" would not be a valid port, and Mew Mewtwo with a substring of "mew" would not be a valid port, but Chimchar Charmander with a substring of "char" would be a valid port.

# About the Python Program
When run, the python program will prompt you to enter -1 to stop, 0 for all pokemon, the gen number (1-8) for all Pokemon of that gen, or 9 for all English words.

The program will construct ports term by term, with each term corresponding to the integer you select.

For example, selecting 2 will output a list of all Gen 2 Pokemon, and then selecting 5 will output all solutions to the port \[Gen 2 Pokemon\] \[Gen 5 Pokemon\]

# About the Discord Bot
The Discord bot uses "." as the command prefix and has .ping and .button as test commands.

The main command to create portmanteaus is .build

.build functions similarly to the python program, except you click buttons instead of inputting integers, and you can choose pokemon types such as \[Fire-Type Pokemon\] as terms of the port whereas the python program only has pokemon generations.

# About the project
I first created this project in C++ in January 2022. I then rewrote the program in python so that I could convert the python program into a Discord bot in April 2022.
