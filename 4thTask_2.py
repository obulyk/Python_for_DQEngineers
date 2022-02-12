import re

countWhiteSpaces = 0
stringSentence = ""
sentence = ""
word = ""
replacedText = ""
t = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.{}



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# text = t.replace('\n', ' ')
textLower = t.lower()
textLower.replace('{}', '')

wordsWithDots = re.findall(r'\w+\.', textLower)
for ele in wordsWithDots:
    stringSentence += ele + ' '
    sentence = stringSentence.lower().replace('.', '')
Str = textLower.format(sentence)
print(Str)

for words in textLower.split():
    editedText = re.sub(r'\biz\b', 'is', textLower)
print(editedText)
# I don't know why it is counting not correctly. Need help
whiteSpaces = re.findall(r'\s', t)
print(whiteSpaces.__len__())