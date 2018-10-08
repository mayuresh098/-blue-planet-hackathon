		
import csv
count=0
with open('names.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		
		if len(row)<1:
			#~ print row,len(row)
			continue
		else:
			print row[0],len(row)
			
		count=count+1
		if count>100:
			break
	
	
