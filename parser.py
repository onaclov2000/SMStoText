import csv

blahs = {}
f = open('/home/tyson/Downloads/sms_20151014.csv', 'rb')
for line in f:
	if line[0:3] == "201":
		row = line.split(',')
		Date = row[0]
		Time = row[1]
		Type = row[2]
		Number = row[3]
		Name = row[4]
		Message = ''.join(row[5:])
		Message = Message.replace('\r\n', '')
		blarg = Name.replace('+', '')		
		if not blarg in blahs:
			blahs[blarg] = 1
		else:
			blahs[blarg] = blahs[blarg] + 1			

sum = 0

import operator

sorted_x = sorted(blahs.items(), key=lambda x: x[1])

for key in sorted_x:
	print key[0] + "," +  str(key[1])
