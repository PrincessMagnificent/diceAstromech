#The idea is to check \downloads for doubled files, the ones that have (1) and such in their filenames
#then delete them?

import re, os

DownloadLoc = "C:\\Users\\Alex\\Downloads"
os.chdir(DownloadLoc)

megaList = os.listdir(os.getcwd())

print len(megaList)