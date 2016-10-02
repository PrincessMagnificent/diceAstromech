import os

print "PROGRAM LOADING...COMPLETE"

#enter the location of the subtitles here, the video files should be in the same directory. But make sure you keep the r in front of the string so that the string is raw and the \ don't get eaten
location = r"H:\tempo\mom\Fringe.Season.1-2-3-4-5.Complete.ILPruny"

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

for index, fileName in enumerate(listOfVideos):
    newName = fileName[:-3:] + "srt"
    print "renaming %s to %s" % (listOfSubs[index], newName)
    #os.rename(listOfSubs[index], newName)
