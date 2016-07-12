import csv, os

print "PROGRAM INITIATED"

listOfDirs = os.listdir(os.getcwd())
print len(listOfDirs), "things, they are", listOfDirs

listOfCSV = []

for filez in listOfDirs:
    if filez.endswith(".csv"):
        ##print filez, "ENDS WITH .CSV YOOOOOOO"
        listOfCSV.append(filez)
    ##else:
    ##    print "FGHAJSDJK", filez, "RAAAAAAAAAAAASK"

print "\nThere are %i CSV files in this directory" % (len(listOfCSV))

##for index, item in enumerate(listOfCSV):
##    print index+1, item

while True:
    try:
        choice = raw_input("select: ")
        choice = int(choice)
    except:
        print "You were meant to give me a number"
        continue
    else:
        print "SELECTED ", listOfCSV[choice-1]
        break
        ##Of course at this point the program breaks if the number is too high