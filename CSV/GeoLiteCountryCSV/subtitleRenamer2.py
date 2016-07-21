import os, re

print "PROGRAM LOADING...COMPLETE"

#enter the location of the subtitles here, the video files should be in the same directory. But make sure you keep the r in front of the string so that the string is raw and the \ don't get eaten
location = r"H:\tempo\mom\Game Of Thrones Complete Season 1, 2, 3 x264 + Extras Multisubs"

print os.getcwd()
##print len(listOfDirs), "things, they are", listOfDirs
os.chdir(location)
print "CHANGING... \n", os.getcwd()

listOfiles = os.listdir(os.getcwd())
listOfSubs = []
listOfVideos = []

for fileName in listOfiles:
    if fileName[-3::] == "srt":
        listOfSubs.append(fileName)
    elif fileName[-3::] == "mp4" or fileName[-3::] == "mkv":
        listOfVideos.append(fileName)

print "videos :", listOfVideos
print "subs :", listOfSubs

listOfVideosRearranged = []
#probably not necessary since videos usually start rearranged

listOfSubsRearranged = []

exPattern = re.compile("[eE]")

for subb in listOfSubs:
    rezult = exPattern.match(subb)
    if rezult:
        print rezult.group()
    else:
        print subb, "Non"