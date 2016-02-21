PURPOSE:
Design and implement feed method for player including strategy, and write test harness for feed portion of evolution game. Write memo on appropriate uses of implemented method.

FILES:

6/feeding contains code for feed implementation

6/feeding/dealer.py is partially written dealer component for attackable project 5

6/feeding/player.py is partially written player component holding the feed method

6/feeding/species.py is the class representing a SpeciesBoard (contains attackable method)

6/feeding/strategy.py is the class containing player strategy for feed

6/feeding/test_attackable.py are the unit tests for the attackable method from project 5

6/feeding/test_player.py are the unit tests for the player component (including feed)

6/feeding/test_species.py are the unit tests for the species file

6/feeding/test_strategy.py are the unit tests for the strategy file

6/feeding/trait.py is the class containing the enumerated Traits

Note: the trait.py file does not have a unit test file due to it being exclusively an enumeration

READING/RUNNING THE CODE:
In order for the code to run you must either be using python version 3.4 or backport using the following command on the command line:
  pip install enum34

All the unit test files (named test_) can be run on the command line by typing 'python <filename>'

To read the feed method code, start in player.py file in the feed method and read into the other files as necessary.

