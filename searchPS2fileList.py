import os, sys

location = "C:\\Users\\Alexc\\Downloads"
fileTarget = "psFileList2016.txt"
positives = []
optionals = []
negatives = []
currentDir = ""

##read the arguments to look for. if the first letter is !, we don't want to search for that. anything else gets searched for.
## & means that it would be nice if the thing is in, but not necessary
arguments = sys.argv[1:]
for argument in arguments:
    if argument[0] == "!":
        negatives.append(argument)
    elif argument[0] == "&":
        optionals.append(argument)
    else:
        positives.append(argument)
print "POSITIVE: ", positives
print "NEGATIVE: ", negatives
print "OPTIONAL: ", optionals

os.chdir(location)
fileListing = open(fileTarget, "r")