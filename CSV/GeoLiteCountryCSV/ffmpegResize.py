import os

print "PROGRAM LOADING...COMPLETE"

#enter the location of the subtitles here, the video files should be in the same directory. But make sure you keep the r in front of the string so that the string is raw and the \ don't get eaten
location = r"O:\eduVideo\Complete Linux Shell Training for Beginners\1 - Introduction to Shell"

print os.getcwd()
##print len(listOfDirs), "things, they are", listOfDirs
os.chdir(location)
print "CHANGING... \n", os.getcwd()

listOfiles = os.listdir(os.getcwd())
listOfVideos = []

for fileName in listOfiles:
    if fileName[-3::] == "mp4" or fileName[-3::] == "mkv":
        listOfVideos.append(fileName)

print listOfVideos

for video in listOfVideos:
    newVideoName = video[:-4:] + "RESIZED.mp4"
    print newVideoName
    newVideoName2 = ""
    for let in newVideoName:
        if let != " ":
            newVideoName2 += let
    kommand = 'ffmpeg -i "' + video + '" -vf scale=1024:-1 ' + newVideoName2
    print kommand
    os.system(kommand)