import string
from sys import argv
import sys

instructions = """subCounter.py takes a standard .srt subtitle file, which has a pattern like this:

1
00:02:56,510 --> 00:02:58,846
This will begin to make things right.

2
00:02:59,764 --> 00:03:02,750
I've traveled too far and seen too much

3
00:03:02,849 --> 00:03:05,812
to ignore the despair in the galaxy.

It then counts how many 'paragraphs' there are in the file, and assigns each its correct number on top. You can either
pass it one argument, the target file, in which case it will just print out, or give it two, the target file and the new
file into which to pass its work."""

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

if argv[1] == "q":
	sys.exit()


if len(argv) == 1:
	print instructions

elif len(argv) == 2:
	paragraphNo = 1
	lines = []
	file = open(argv[1],"r")

	for line in file:
		lines.append(line)

	for x in range(30):
		if len(lines[x]) == 2:
			paragraphNo += 1
			print "+++++++++++++++++++",
		try:
			print int(lines[x]), "NUMBAH"
		except:
			print paragraphNo,"||  ", len(lines[x]), lines[x]

	file.close()

elif len(argv) == 3:
	print "there are two arguments, %s is the source and %s is the new file name" % (argv[1],argv[2])
else:
	print "YOU PASSED TOO MANY ARGUMENTS!\n",instructions,"\nYOU PASSED TOO MANY ARGUMENTS"

	##TODO
	"""
	The ultimate goal of this program is to take a .srt subtitle file and count how many subtitles are in it. .srt files have an index that tells you what time the subtitle is supposed to appear at, and also which subtitle in order it is. This makes it a problem to edit subtitle files because if you add or remove a subtitle, all the index numbers become wrong, which is unhelpful.

	So I want this program to check all the index numbers and make them right -> 1,2,3,4,5,6 again
	"""
