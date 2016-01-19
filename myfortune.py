import random
import os

filename = "myfortunes.txt"
subdir = "~/Documents/CS/python/"
expandeddir = os.path.expanduser("~/Documents/CS/python/myfortunes/")
fortunefile = open(os.path.join(expandeddir, filename))

lc = 0
for i, line in enumerate(fortunefile):
	lc = i
lc+=1
randInt = random.randrange(0,lc)

fortunefile.close()
fortunefile = open(os.path.join(expandeddir, filename))

for i, line in enumerate(fortunefile):
	if randInt == i:
		print line

fortunefile.close()

