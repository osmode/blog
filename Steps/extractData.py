import urllib2
import json
import datetime

response = urllib2.urlopen('http://api.naveen.com/v0/steps?at=56122cc6-6a6e-4699-95a2-b4f1ec9c5f50')

pyresponse = json.load(response)
m = len(pyresponse)
fileout = open("output2",'w')

print type(pyresponse)

old_year = int(pyresponse[0]["date"][0:4])
old_month = int(pyresponse[0]["date"][5:7])
old_date = int(pyresponse[0]["date"][8:10])

year_list = []
month_list = []
date_list = []
day_list = []
steps_list = []

# pyresponse is a list of dictionaries
for i in pyresponse:
	
	year = i["date"][0:4]
	year = int(year)
	year_list.append(year)

	month = i["date"][5:7]
	month = int(month)
	month_list.append(month)

	date = i["date"][8:10]
	date = int(date)
	date_list.append(date)

	dateObj = datetime.date(year,month,date)

	# Monday --> day = 0
	day = dateObj.weekday()
	day_list.append(day)

	steps = i["value"] 
	steps_list.append(steps)

print len(day_list)
print len(steps_list)
print m
# print out 3 columns: day (Monday=0), steps, 
# steps of prior day
i = m-2
while i > 0:
		
	fileout.write(str(day_list[i]))
	fileout.write(',')
	fileout.write(str(steps_list[i]))
	fileout.write(',')
	fileout.write(str(steps_list[i+1]))
	#fileout.write(',')
	fileout.write('\n')

	i -= 1

fileout.close()

