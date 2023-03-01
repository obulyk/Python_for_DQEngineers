from datetime import datetime, date
import pickle
"""Description
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format
You need to implement:
1. News – text and city as input. Date is calculated during publishing.
2. Privat ad – text and expiration date as input. Day left is calculated during publishing.
3. Your unique one with unique publish rules.
Each new record should be added to the end of file. Commit file in git for review."""
filename = str('/Users/ok/PycharmProjects/Python_for_DQEngineers/file.txt')
#with open(filename,'a')
f = open(filename, 'r+')
f = open(filename, 'a')
#print(dir(filename.__add__))
def selectTypeNews():
    print("Please select a type of news:\n 1 - news, 2 - ads, 3 - ukrainian-russia war.")
    mode = input()
    if mode == '1':
        return News(input('Type in the text of an article that you want to publish: '), input('Input city: '), datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    elif mode == '2': return Ads(input('Type in the text of an advertisement:'), input('Type in expiration date in format DD/MM/YYYY:'))
    elif mode == '3': return MyRules("%d/%m/%Y")
    else: print("Must be 1 or 2 or 3. Check if you enter such numbers.")
class News():
    def __init__(self, textOfArticle, city, dt):
        self.textOfArticle = textOfArticle
        self.city = city
        self.dt = dt
        n = "-----News------"
        f.write(n + '\n' + textOfArticle + '\n' + city + '\n' + dt + '\n')
class Ads():
    def __init__(self, textOfads, expirationDate):
        self.textOfads = textOfads
        self.expirationDate = expirationDate
        a = ("----Advertisement----")
        dt = datetime.strptime(datetime.now().strftime("%d/%m/%Y"),("%d/%m/%Y")).date()
        dNow = datetime.strptime(expirationDate,("%d/%m/%Y")).date()
        expDate = dNow-dt
        f.write(a + '\n' + textOfads + '\n' + str(dNow) + '\n' + "Days till advertisement is valid: "+str(expDate.days)+'\n')

class MyRules():
    def __init__(self, diff):
        self.diff = diff
        count_years = 0
        m = ("----Uraine-russia war----")
        date_start = datetime.strptime("24/02/2022", "%d/%m/%Y")
        date_end = date.today()
        date_end = datetime(date_end.year,date_end.month,date_end.day)
        diff = date_end - date_start
        days = diff.days
        while (days >= 365):
            count_years += 1
            days = days - 365
        f.write(m + '\n' + "Ukrainian-russia war lasts: " + str(count_years) + " year and " + str(days) + " days"+'\n\n')
selectTypeNews()
#f.write(str(selectTypeNews()))