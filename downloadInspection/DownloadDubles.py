#The idea is to check \downloads for doubled files, the ones that have (1) and such in their filenames
#then delete them?

import re, os

def ls():
    return os.listdir(os.getcwd())

DownloadLoc = "C:\\Users\\Alexc\\Downloads"
os.chdir(DownloadLoc)

megaList = ls()
evilList = []

print len(megaList), "files"

#match digits in re with \d
#explication of pattern:
#.* = any number of symbols
#\( and \) are the brackets
#\d for a single number
patternRE = r".*\(\d.\)*\.\w\w\w"

for listItem in megaList:
    if re.match(patternRE,listItem):
        evilList.append(listItem)

print evilList

for doppler in evilList:
    os.remove(doppler)

    ##AND IT FUCKING WORKS, YAY!!