import os

theFile = open("srchMp4.txt","r")
print "opened it!"
maxFile = ""

#ffprobe -i 025\ HTML5\ Game\ runaway\ ghost.mp4 -show_entries format=duration -v quiet -of csv="p=0"
kommandSTART = "ffprobe -i "
kommandEND = " -show_entries format=duration -v quiet -of csv='p=0'"

MAXIMUS = [0,""]
lineITER = 0
for line in theFile:
    lineITER += 1
    if lineITER > 1:
        realKommand = kommandSTART + line.strip() + kommandEND
        #print realKommand  
        os.system(realKommand)
        result = os.system(realKommand)
        if result != 256:
            print result


theFile.close()

##it doesn't work yet
##I think the problem are the spaces in the file name
##make sure you make it a raw string by going x = r"/dog years/" or whatever