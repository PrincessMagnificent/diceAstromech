import csv, os

print "PROGRAM INITIATED"

listOfDirs = os.listdir(os.getcwd())
print len(listOfDirs), "things, they are", listOfDirs

for filez in listOfDirs:
    if filez.endswith(".csv"):
        print filez, "ENDS WITH .CSV YOOOOOOO"
    else:
        print "FGHAJSDJKASJKDKJASDJKKASDJKASDJAKSJDAKSJDKASJDAKSJD"

###How do you like this