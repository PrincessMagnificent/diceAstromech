from random import randint
import string
##BASIC STAR WARS DICEROLLER
##Based on the Under A Black Sun PDF
        
def diceFinder(command,target):
    numbaList = "1234567890"
    sides = ""
    for indx, val in enumerate(command):
        if val == target and command[indx+1] in numbaList:
            for x in command[indx+1:]:
                if x not in numbaList:
                    break
                else:
                    sides += x
    if sides != "":
        return int(sides)
    else:
        return 1
        
def roller(command,target):
    die = diceFinder(command,target)
    print type(die)
    print "%s%i = %i" % (target,die,randint(1,die))
        
command = ""
while command != "quit":
    command = raw_input(">>")
    helpasks = ["help","Help","HELP","h","H","F1"]
    if command in helpasks:
        print "type in d# to roll a #-sided die. That's the only functionality available right now. \n Oh, and \"quit\" quits."
    elif command != "quit":
        roller(command,"d")
        
### So now it can check for a d8 and find it. Nice. But the problem is that if the string is "I like d8 and d8, it thinks that the die is 88.
