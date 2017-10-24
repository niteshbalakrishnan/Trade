import NSE_Trade.FileNew
import csv
import os
#import NSE_Trade.Database

cv = NSE_Trade.FileNew
# db = NSE_Trade.Database
c = cv.csvfile()
action= input("Enter command")
#c.daily_price('C:\Phython Projects\cm29MAY2017bhav.csv')

if action == 'D':
    filename=   input("Input Daily File Name")
    filenm = 'P:\\Nitesh\\Peoplesoft-Activity\\Issue List\\Issue2412\\Price History'+'\\'+ filename
    c.daily_price(filenm)
if action == 'I':
    filename = input("Input Indicator File Name")
    filenm = 'P:\\Nitesh\\Peoplesoft-Activity\\Issue List\\Issue2412\\Indicator' + '\\' + filename
    c.daily_indicator(filenm)
if action == 'C':
    filename = input("Load from HTML page")
    filenm = 'C:\\Nitesh\\' + "todays_file.csv"
    c.loadhtmlclose(filenm)
if action == 'U':
    ff = input("Generating URL List")
    filename = 'C:\\Nitesh\\list.csv'
    wrfilename = 'C:\\Nitesh\\list_url.csv'
    c.generate_url(filename,wrfilename)
if action == 'T':
    ff = input("Loading todays file")
    filename = 'C:\\Nitesh\\todays_file.csv'
    c.todays_file(filename)
if action == 'UM':
    filename=   input("Input Daily File Name")
    c.insert_monthly_data(filename)

if action == 'FD':
    upload_file = 'C:\\Nitesh\\upload_list.csv'
    with open(upload_file, newline='') as csvfile:
        sp = csv.reader(csvfile)
        for row in sp:
            filenm = 'P:\\Nitesh\\Peoplesoft-Activity\\Issue List\\Issue2412\\Price History' + '\\' + row[0]
            c.daily_price(filenm)
if action == 'ST':
    c.update_stat()