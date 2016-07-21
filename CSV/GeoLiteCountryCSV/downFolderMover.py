import os

print "PROGRAM LOADING...COMPLETE"

#enter the location of the subtitles here, the video files should be in the same directory. But make sure you keep the r in front of the string so that the string is raw and the \ don't get eaten
location = r"H:\tempo\mom\The Blacklist Season 3 S03  Complete 720p ~{KiNg}"

print os.getcwd()
##print len(listOfDirs), "things, they are", listOfDirs
os.chdir(location)
print "CHANGING... \n", os.getcwd()

listOfiles = os.listdir(os.getcwd())
listOfDirs = []

print listOfiles

#assuming that the file ending is 3 letters long, then item[-4:-3:] is the dot that lets me tell folders apart from files

for item in listOfiles:
    if item[-4:-3:] != ".":
        listOfDirs.append(item)

print listOfDirs
print "and they're all in " + location

print os.listdir(location + "\\" + listOfDirs[0])

for direktory in listOfDirs:
    os.chdir(location + "\\" + direktory)
    fileInside = os.listdir(os.getcwd())[0]
    os.rename(fileInside,"..\\" + fileInside)

#you can move a file up the folder tree by saying os.rename("file.txt", "..\\file.txt")