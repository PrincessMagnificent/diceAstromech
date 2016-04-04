# diceAstromech
Python 2.7 program that looks at a string and finds dice rolling commands in it.

The idea right now is that it asks you for input, and you can type in something like "Gosh, I'd really love it if you rolled a d20 for me." Then it sees "d20" and provides a random number between 1 and 20.

CURRENT ISSUES:
Can only roll one die at a time.
The string "I like d8s, I really like d8s" will make it think you want to roll a d88.

Eventually, I will want it to look at different TYPES of dice and return different results based on them, so it won't all hinge on "d". Part of this is because I want an IRC dicebot that can run Edge of Empire games, a Star Wars tabletop RPG with very strange dice that give you results of how many Successes and Advantages you have. 

#subCounter.py

This baby is useful for repairing .srt subtitle files.
What it does is check the first number in front of each paragraph and make sure they're all one after the other.
This will be very useful when I create my translation of the Force Awakens, where I will need to add slovenian
translations of the crawl, which the english version does not have.