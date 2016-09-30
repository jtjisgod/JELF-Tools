import os
import sys

##############################################
#                                                                                                   #
#    Copyright (c) 2016 Copyright JTJ All Rights Reserved.     #
#                                                                                                   #
##############################################

####################################
# Title 		: JTJElfString.py 	                       #
# Author	: JTJ     ( jtjisgod @ gmail . com ) #
# Last Fix 	: 2016.09.30. Fri. 13:32	       #
####################################

print
print
print

binary = raw_input("Elf File name : ")

search = raw_input("Search Text : ") # "/bin/sh"

print
print

# sh = Section Header
sh = os.popen("readelf -S ./" + binary).read()

output = ""

shList = sh.split("\n")

bbs = None

for sh in shList :

	output = sh.split(" .")
	
	try :
		if output[1].split(" ")[0] == "bss" :
			bbs = output[1].split(" ")[24]

	except :
		pass


hexcode = os.popen("objdump -s ./" + binary).read()

a = hexcode.split("\n")

for searchLen in range(0, len(search)) :
	print
	print
	print
	print search[searchLen:searchLen+1]
	for i in a :
		i = "0x" + " ".join(i.split(" ")[1:len(i.split(" "))]);
		if i.find("of section") == -1 and i.find("file format") == -1:
			if i[0:4] != "0x00" and len(i) > 10:
				## memory
				# 0 : Pointer
				# 1 : First Memory (4byte)
				# 2 : Second  Memory (4byte)
				# 3 : Third  Memory (4byte)
				# 4 : fourth  Memory (4byte)
				##
			
				memory = i.split(" ")[0:4]

				for j in range(1,4) :

					alphabet = search[searchLen:searchLen+1]

					memoryByte = len(memory[j]) / 2

					for k in range(0,memoryByte) :
						char = memory[j][k*2:(k+1)*2]
						if chr(int("0x" + char, 0)) == alphabet :
							h = (hex(int(memory[0],0) + k))
							print str(h) + " ",




print
print
print
print

print "BSS Address : 0x" + bbs

print
print
print

