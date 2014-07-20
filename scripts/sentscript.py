##This gets you a sentiment for the dictionary

from sampledata import *
from string import ascii_letters
import os

<<<<<<< HEAD
DATA_PATH = os.getcwd()+ '\\'
=======
DATA_PATH = ""
>>>>>>> origin/master

def load_sentiments(file_name=DATA_PATH + "sentiments.csv"):
    """Read the sentiment file and return a dictionary containing the sentiment
    score of each word, a value from -1 to +1.
    """
    sentiments = {}
    for line in open(file_name, encoding='utf8'):
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


duke = datadict['2014/02/19/bkc-duke-georgiatech-writethru-idUSMTZEA2J86BZRT20140219']


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
    return (totalSentiment/n)

def getAllArticleSentiment(datadict = datadict):
    returnDict = {}
    for key in datadict:
        article = datadict[key]
        returnDict[key] = getArticleSentiment(datadict[key])
    return returnDict

sentimentDictionary = getAllArticleSentiment(datadict)


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

def searchFunction(keyword):
    keyword = keyword.lower()
    listOfIDs = [] # a list of IDs whose articles have the keyword in the text
    for ID in datadict:
        if keyword in strToLst(get('text', datadict[ID])):
            listOfIDs.append(ID)
    return sentimentByDate(listOfIDs)