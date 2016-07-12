import os

print "PROGRAM LOADING...COMPLETE"


#enter the location of the subtitles here, the video files should be in the same directory. But make sure you keep the r in front of the string so that the string is raw and the \ don't get eaten
location = r"H:\tempo\mom\The.Blacklist.S01.HDTV.x264-LOL\1_titlovi"

print os.getcwd()
##print len(listOfDirs), "things, they are", listOfDirs
os.chdir(location)
print "CHANGING... \n", os.getcwd()

listOfiles = os.listdir(os.getcwd())
print len(listOfiles)
print listOfiles[3]

for x in listOfiles:
    print x[-4::]