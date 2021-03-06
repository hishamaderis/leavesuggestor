import csv
import datetime
import json
from pprint import pprint
from termcolor import colored, cprint

year = ''
leave = ''

def maxLeave(leave):
	if leave == '1':
		with open('2016.csv', mode='r') as infile:
			reader = csv.reader(infile)
	#with open('2016.csv', mode='w') as outfile:
	#    writer = csv.writer(outfile)
			mydict = {rows[0]: rows[1] for rows in reader}
			print ("You can apply a leave on:")
			for k,v	in mydict.items():
				if v == 'Monday':
					print ("Friday before, or Tuesday after " + colored(k,'green') + " to get maximum numbers of leave, which is 4 days\n")
				if v == 'Tuesday':
					print ("Monday before " + colored(k,'yellow') + " to get maximum numbers of leave, which is 4 days\n")
				if v == 'Thursday':
					print ("Friday after " + colored(k,'blue') + " to get maximum numbers of leave, which is 4 days\n")
				if v == 'Friday':
					print ("Thursday before, or Monday after  " + colored(k,'magenta') + " to get maximum numbers of leave, which is 4 days\n")
	elif leave == '2':
		with open('2016.csv', mode='r') as infile:
			reader = csv.reader(infile)
			mydict = {rows[0]: rows[1] for rows in reader}
			print ("You can apply a leave on:")
			for k,v	in mydict.items():
				if v == 'Monday':
					print ("Tuesday and Wednesday after, or Thursday and Friday before " + colored(k,'green') + " to get maximum numbers of leave, which is 5 days\n")
				if v == 'Tuesday':
					print ("Friday and Monday before " + colored(k,'yellow') + " to get maximum numbers of leave, which is 5 days\n")
				if v == 'Wednesday':
					print ("Monday and Tuesday before, or Thursday and Friday after " + colored(k,'cyan') + " to get maximum numbers of leave, which is 5 days\n")
				if v == 'Thursday':
					print ("Thursday and Friday after " + colored(k,'blue') + " to get maximum numbers of leave, which is 5 days\n")
				if v == 'Friday':
					print ("Monday and Tuesday after " + colored(k,'magenta') + " to get maximum numbers of leave, which is 5 days\n")
	elif leave == '0':
		print ("You don't need this program if you are not willing to apply for any leave")
	else:
		print ("We only cater for 1 and 2 days of annual leave for the moment, sorry for any inconvenience :)")

def yearIn(y):
	if y == '':
		y = input("Please put in the year that you are interested in: ")
		yearIn(y)
	elif y == '2016':
		print ("You have put in " + y)
		leave = input("How many days of leave are you going to apply?: ")
		print ("and you are willing to apply for " + leave + " day/s")
		maxLeave(leave)
		return y
	else:
		print ("Sorry, we only have 2016 in our record for the time being")

yearIn(year)
