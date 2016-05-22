import csv, sys

print "I am lost in the sea of stars"

with open("testBunny.csv",mode="r") as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        print len(row), row, type(row)
        for item in row:
            print len(item),

##What does it look like unsaved