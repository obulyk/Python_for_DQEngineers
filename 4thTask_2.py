import re

global t
t = """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.{}

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# t.replace('{}', '')
countWhiteSpaces = 0
global stringSentence
global text

def letterLowerCases(t):
    global textLower
    textLower = t.lower()
    text = textLower.replace('{}', '')
    return text

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

def missSpellingFixedText(t):
    words = ""
    for words in t.split():
        editedText = re.sub(r'\biz\b', 'is', t)
    return print(editedText)

def findAllWhiteSpaces(t):
    whiteSpaces = re.findall(r'\s', t)
    return print(whiteSpaces.__len__())
findAllWhiteSpaces(t)


