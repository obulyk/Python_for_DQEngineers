import re

global t
t = """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.{}

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

countWhiteSpaces = 0
global stringSentence

def letterLowerCases(t):
    global textLower
    textLower = t.lower().replace('{}', '')
    # for i in textLower:
    #     if textLower[i]. ==".":print ("wwwww")
    return textLower
print(letterLowerCases(t))
def lastWordsSentence(t):
    letterLowerCases(t)
    import re
    sentence = ""
    stringSentence = ""
    wordsWithDots = re.findall(r'\w+\.', textLower)
    for ele in wordsWithDots:
        stringSentence += ele + ' '
        sentence = stringSentence.lower().replace('.', '')
    oneStr = textLower.format(sentence)
    return oneStr
#print(lastWordsSentence(t))

def missSpellingFixedText(func):
    letterLowerCases(t)
    for word in textLower:
        ch_text = re.sub(r'\biz\b', 'is', textLower)
    return (ch_text.replace('{}', ''))
#print (missSpellingFixedText(t))

def findAllWhiteSpaces(t):
    print(missSpellingFixedText(t))
    t.lower()
    whiteSpaces = re.findall(r'\s', t)
    return print(whiteSpaces.__len__())
#findAllWhiteSpaces(t)


