#jsonthingy

from sentscript import *
from sentimentDictionary import *
import json
import os

DATA_PATH = os.getcwd()+ '/'
keywordFile = ''

#write data

current = open(DATA_PATH+'keyword.txt', 'r+').read()
if current != keywordFile:
    print(current)
    rv = '[Date, Values]'
    new_values = (searchFunction(current))
    with open(DATA_PATH + "dump.csv", "w") as outfile:
        if type(new_values) == float:
            json.dump(new_values,outfile)
        else:
            outfile.write(rv+'\n')
            for key in new_values:
                json.dump(str([dateChanger(key),new_values[key]]), outfile, indent=2)
                outfile.write('\n')
    keywordFile = current

#clean data

with open(DATA_PATH + "dump.csv", "r+") as outfile:
	inPut = outfile.read()
	outPut = ''
	for i in range(len(inPut)):
		if inPut[i] not in ['"', '[', ']', "'"]:
			outPut += inPut[i]

#rewrite data
with open(DATA_PATH + "dump.csv", "w") as outfile:
	outfile.write(outPut)










# # keyword = json.load(asdflkja;sdkfj; keyword)
# # json.dump(searchFunction(keyword))

# bulkData = searchFunction('one')

# import httplib,json,urllib
# headers = { "charset":"utf-8", "Accept": "text/plain"}
# conn = httplib.HTTPConnection("localhost")
# #converting list to a json stream
# bulkData = json.dumps(bulkData, ensure_ascii = 'False')
# # ensure_ascii is false as data is in unicode and not ascii encoding , use this if data is in any other encoding
# postData = urllib.urlencode({'results':bulkData})
# conn.request("POST", "/getresult.php", postData,headers)
# # response = conn.getresponse()
# # text = response.read()
# # print (response.status,text)
# # conn.close()

