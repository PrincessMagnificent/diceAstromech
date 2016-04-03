import string
from sys import argv


##the usual enumerate
def printnumerate(thing):
	for index, element in enumerate(thing):
		print index, element

##a special enumerate that also prints the length of whatever it is enumerating, if possible
def printnumerate2(thing):
	for index, element in enumerate(thing):
		try:
			print "indx%i - (len%i) - %s" % (index, len(element), element)
		except:
			print index, element

printnumerate(argv)

lines = []
file = open(argv[1],"r")

for line in file:
	lines.append(line)

print "ze length of ze file is", len(lines),"\n"

printnumerate2(lines)

##TODO
"""
The ultimate goal of this program is to take a .srt subtitle file and count how many subtitles are in it. .srt files have an index that tells you what time the subtitle is supposed to appear at, and also which subtitle in order it is. This makes it a problem to edit subtitle files because if you add or remove a subtitle, all the index numbers become wrong, which is unhelpful.

So I want this program to check all the index numbers and make them right -> 1,2,3,4,5,6 again
"""
