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

def selectTypeNews():
    print("Please select a type of news:\n 1 - news, 2 - ads, 3 - Your unique one with unique publish rules.")
    try:
        mode = int(input())
    except ValueError:
        print("Not a number")
    if mode == 1: print("News")
    elif mode == 2: print("ads")
    elif mode == 3: print("unique publish rules")
class News():
    self:
    selectTypeNews()

class Ads():
    pass
class MyRules():
    pass

selectTypeNews()