import json
from pprint import pprint

json_data = open('data.json')

data = json.load(json_data)
# pprint(data)

dates = data["Dates"]
price = data["Elements"][0]["DataSeries"] ["close"]["values"]

def convertDate(aStr):
	year = aStr[:4]
	month = aStr[5:7]
	day = aStr[8:10]
	return month + '/' + day + '/' + year

rDict = {}
for i in range(len(dates)):
	rDict[convertDate(dates[i])] = price[i]


with open('stock.csv', 'w') as outfile:
	outPut = 'Date, Price\n'
	for elem in rDict:
		outPut +=  elem + ', ' + str(rDict[elem]) + '\n'
	outfile.write(outPut)

