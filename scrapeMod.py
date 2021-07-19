import urllib.request
from urllib.request import Request, urlopen

def scrape(url,frontBackList): 
    # front back pair structure: [(front,back),(front,back),...]
    resultList = []
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    rawWeb = urlopen(req).read()

    webString = rawWeb.decode('UTF-8')
    for pair in frontBackList:
        front = pair[0]
        back = pair[1]
        if front in webString:
            i = webString.find(front)
            possible = webString[i+len(front):]
            i2 = possible.find(back)
            if i2 != -1:
                resultList.append(possible[0:i2])
            else:
                resultList.append("")
        else:
            resultList.append("")

    
    return resultList
                


def printAll(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    f = webpage.decode('UTF-8')
    print(type(f))
    print(f)
    """
    for row in webpage:
        rowString = str(row)
        print(rowString)
    """

def scrapeTest(url,seekString):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    rawWeb = urlopen(req).read()
    stringsToCheck = []
    rowString = rawWeb.decode('UTF-8')
    if seekString in rowString:
        limit = len(rowString)
        start = 0
        end = 100
        while end < limit:
            stringsToCheck.append(rowString[start:end])
            start += 50
            end += 50
        stringsToCheck.append(rowString[start:limit-1])
    toPrint = []
    for s in stringsToCheck:
        if seekString in s:
            i = s.find(seekString)
            if i + 49 < 100:
                possible = s
                toPrint.append(possible)
    
    for each in toPrint:
        print(each)
