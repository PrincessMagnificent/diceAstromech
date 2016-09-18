import string

theFile = open("searchResult.txt","r")
print "opened it!"
lineNum = 0
fileTypeList = []

for line in theFile:
    lineNum += 1
    
    fileType = string.lower(line[-5::])
    if fileType not in fileTypeList:
        fileTypeList.append(fileType)
    
print "there are " + str(lineNum) + "lines"

for typexxx in fileTypeList:
    print typexxx

theFile.close()

##With this I have discovered that the main videos are .m4a and .mp4