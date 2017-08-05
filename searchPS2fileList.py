import os, sys

location = "C:\\Users\\Alexc\\Downloads"
fileTarget = "psFileList2016.txt"
positives = []
optionals = []
negatives = []
currentDir = ""
previousDir = ""
toggleFlag = 0

def findTags(line,positives,optionals):
    global toggleFlag
    global previousDir
    searchTags(line,positives,optionals)
    if toggleFlag == 1:
        if currentDir != previousDir:
            print "\n", "#"*40, "\n", currentDir
            previousDir = currentDir
        print line,
    toggleFlag = 0


def searchTags(line,positives,optionals):
    global toggleFlag
    for optional in optionals:
        if optional.lower() in line.lower():
            toggleFlag = 1

    for positive in positives:
        if positive.lower() not in line.lower():
            toggleFlag = 0
        else:
            toggleFlag = 1

    ##comment out this portion to avoid scanning directories as well
    for negative in negatives:
        NEOcurrentDir = currentDir.replace("\\","\\\\")
        if negative.lower()[1:] in NEOcurrentDir.lower():
            toggleFlag = 0


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
for line in fileListing:
    if line[0:2] == "e:":
        currentDir = line
    if len(negatives) > 0:
        for negative in negatives:
            if negative[1:].lower() not in line.lower():
                findTags(line, positives, optionals)
    else:
        findTags(line,positives, optionals)

##current issue: directories aren't searched by name?

l = [1,2,3]
l.