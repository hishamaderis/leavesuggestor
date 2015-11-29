import csv
import datetime
import json
from pprint import pprint

year = input("Please put in the year of your interest: ")

if year == '2016':
    print ("You have put in " + year)
    leave = input("How many days of leave are you going to apply?: ")
    print ("and you are willing to apply for " + leave + " day")
    with open('2016.csv', mode='r') as infile:
        reader = csv.reader(infile)
    #with open('2016.csv', mode='w') as outfile:
    #    writer = csv.writer(outfile)
        mydict = {rows[0]: rows[1] for rows in reader}
        print ("You can apply a leave on:")
        for k,v	in mydict.items():
            if v == 'Monday':
                print ("Friday before " + k + " or Tuesday after " + k + " to get maximum numbers of leave, which is 4 days")
    #print (mydict)

else:
    print ("Sorry, we only have 2016 in our record for the time being")
