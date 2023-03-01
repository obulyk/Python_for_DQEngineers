"""Expand previous Homework 5 with additional class, which allow to provide records by text file:

  1.Define your input format (one or many records)
  2.Default folder or user provided file path"""
from datetime import datetime, date

filename = str('/Users/ok/PycharmProjects/Python_for_DQEngineers/file.txt')
f = open(filename, 'r+')
f = open(filename, 'a')


# print(dir(filename.__add__))
def selectTypeNews():
    print("Please select a type of news:\n 1 - news, 2 - ads, 3 - ukrainian-russia war, 4 -TO READ FROM FILE")
    mode = input()
    if mode == '1':
        return News(input('Type in the text of an article that you want to publish: '), input('Input city: '),
                    datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    elif mode == '2':
        return Ads(input('Type in the text of an advertisement:'),
                   input('Type in expiration date in format DD/MM/YYYY:'))
    elif mode == '3':
        return MyRules("%d/%m/%Y")
    elif mode == '4':
        file_reader = RecordFileReader('/Users/ok/PycharmProjects/Python_for_DQEngineers/Readfile1.txt')
        records = file_reader.read_records_from_file()
        return records
    else:
        print("Must be 1 or 2 or 3 or 4 -TO READ FROM FILE. Check if you enter such numbers.")


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
        dt = datetime.strptime(datetime.now().strftime("%d/%m/%Y"), ("%d/%m/%Y")).date()
        dNow = datetime.strptime(expirationDate, ("%d/%m/%Y")).date()
        expDate = dNow - dt
        f.write(a + '\n' + textOfads + '\n' + str(dNow) + '\n' + "Days till advertisement is valid: " + str(
            expDate.days) + '\n')


class MyRules():
    def __init__(self, diff):
        self.diff = diff
        count_years = 0
        m = ("----Uraine-russia war----")
        date_start = datetime.strptime("24/02/2022", "%d/%m/%Y")
        date_end = date.today()
        date_end = datetime(date_end.year, date_end.month, date_end.day)
        diff = date_end - date_start
        days = diff.days
        while (days >= 365):
            count_years += 1
            days = days - 365
        f.write(
            m + '\n' + "Ukrainian-russia war lasts: " + str(count_years) + " year and " + str(days) + " days" + '\n\n')


class RecordFileReader():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_records_from_file(self):
        records = []
        with open(self.file_path, 'r',) as f:
            for line in f:
                record = line.strip().split('-')
                records.append(record)
            for i in records:
                print(records[i])

selectTypeNews()
