import sys

#req=3
cur=sys.version_info
if cur>=(3,0):
	print ("You are good to go")
else:
	print ("You need python 3 or above")