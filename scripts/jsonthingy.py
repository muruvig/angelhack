#jsonthingy

from sentscript import *
import json
import os

DATA_PATH = os.getcwd()+ '\searching\\'
keywordFile = ''


current = open(DATA_PATH+'keyword.txt', 'r+').read()
if current != keywordFile:
	with open(DATA_PATH + "dump.json", "w") as outfile:
		json.dump(searchFunction(current), outfile)
	keywordFile = current














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

