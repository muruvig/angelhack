##This gets you a sentiment for the dictionary

from betterdata2 import *
from betterdata3 import *
from betterdata4 import *
from string import ascii_letters
import os

a = {}
for letter in [a,b,c]:
	for elem in letter:
		a.update(elem)
datadict = a
DATA_PATH = os.getcwd()+ '/'

def load_sentiments(file_name=DATA_PATH + "sentiments.csv"):
    """Read the sentiment file and return a dictionary containing the sentiment
    score of each word, a value from -1 to +1.
    """
    sentiments = {}
    ######################    open(file_name).replace("\n", " ")##################
    for line in open(file_name):#, encoding='utf8'):
        word, score = line.split(',')
        sentiments[word] = float(score.strip())
    return sentiments

word_sentiments = load_sentiments()


def get_word_sentiment(word):
    try:
        return word_sentiments[word]
    except:
        return 0

def strToLst(aStr):
    """
    strToLst('Hello, my name is Bob')
    """
    aStr = str(aStr)
    aStr.encode('utf-8')
    aStr += '.'
    words = []
    word = ''
    for i in range(len(aStr)):
        if aStr[i] in ascii_letters:
            word += aStr[i].lower()
        else:
            if word != '':
                words.append(word)
            word = ''
    return words


##data abstraction for articles
def get(key, article):
    if key == 'title':
        return article[0]
    if key == 'date':
        return article[1]
    if key == 'text':
        return article[2]
    else:
        print('Bad key')



def getArticleSentiment(article):
    """
    Given an article in the form [title, data, text], returns the
    average sentiment of the article
    """
    text = strToLst(get('text', article))
    totalSentiment, n = 0, 0
    for aWord in text:
        totalSentiment += get_word_sentiment(aWord)
        n += 1
    try:
    	return (totalSentiment/n)
    except:
    	return (totalSentiment)

def getAllArticleSentiment(datadict = datadict):
    returnDict = {}
    for key in datadict:
        article = datadict[key]
        returnDict[key] = getArticleSentiment(datadict[key])
    return returnDict

def createSentDict():
	sentimentDictionary = getAllArticleSentiment(datadict)
	with open(DATA_PATH+'\sentimentDatabase.py', 'w') as outfile:
		outfile.write('sentimentDictionary = ' + str(sentimentDictionary))

from sentimentDictionary import *

def sentimentByDate(listOfIDs): #returns a dictionary of date:averageSentiment
    returnDict = {}
    for ID in listOfIDs:
        date = get('date', datadict[ID])
        text = get('text', datadict[ID])
        if date not in returnDict:
            returnDict[date] = [sentimentDictionary[ID]]
        elif date in returnDict:
            returnDict[date].append(sentimentDictionary[ID])
    #by now, returnDict = {date:[list of sentiments]}
    for key in returnDict:
        totalSent = 0
        for sentiments in returnDict[key]:
            totalSent += sentiments
        avgSent = totalSent/len(returnDict[key])
        returnDict[key] = avgSent
    return returnDict

def dateChanger(dateStr):
	return dateStr[5:] + '/' + dateStr[0:4]

def searchFunction(keyword, avg = False):
    keyword = keyword.lower()
    listOfIDs = [] # a list of IDs whose articles have the keyword in the text
    for ID in datadict:
        if keyword in strToLst(get('text', datadict[ID])):
            listOfIDs.append(ID)
    rV = sentimentByDate(listOfIDs)
    if avg == True:
    	total, n = 0, 0
    	for elem in rV:
    		total += rV[elem]
    		n+=1
    	try:
    		return total/n
    	except ZeroDivisionError:
    		return 'Not mentioned in any articles'
    return rV
