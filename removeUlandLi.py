import re, os, sys

location = r"C:\Users\alexc\gitStuff\princessmagnificent.github.io"
fileTarget = "timeCYOA.html"


try:
    os.chdir(location)
    print("changing location to " + location)
    openedFile = open(fileTarget, "r")
    print("opening file " + fileTarget)

    


    openedFile.close()
    print("it worked")
except:
    print("NOPE")
