'''
This file implements multiple helper functions that receive, extract, read and
do other stuff with the data

'''

import pandas as pd
import json
import os
import re

def get_files(path = None):
	if path:
		return os.listdir()
	else:
		return os.listdir(os.path.dirname(os.path.realpath(__file__)))

def get_people(file,i = 0,j = -1):
	file = pd.read_csv(file)
	data = file.loc[i:j,["company","email"]] 
	return data


def filter_files(files, extension):
	r = re.compile('.*'+extension)
	return list(filter(r.match, files))


def read():

	if input("try to read from saved.json? (y/n)").lower() == 'y':
		try:
			data = open('saved.json','r')
			d = json.load(data)
			fromU = d['fromU']
			sub = d['sub']
			body = d['body']
			attach = d['attach']
			return (fromU, sub, body, attach)
		except:
			print("couldn't read data from saved.json, please enter data again")
	
	fromU = input("From :")
	sub = input("sub :")
	
	if input("enter body from file? (y/n) ").lower() == 'y':
		if input("enter a path? (y/n) ").lower() == 'y':
			path = input('path :')
			files = get_files(path)
		else:
			files = get_files()
		text_files = filter_files(files, '\\.txt')
		if len(text_files) > 0:
			for i in range(len(text_files)):
				print(i+1,'. ',text_files[i])
			choice = -1
			while choice not in range(len(text_files)):
				choice = int(input('choose file number to read body from :'))
			body = open(text_files[choice],'r').read()
		else:
			print("couldn't find any text files")
			body = input('body :')
	else:
		body = input('body :')
	files = get_files()
	for i in range(len(files)):
		print(i,'. ',files[i])
	choice = -2
	while choice not in range(-1,len(files)):
		choice = int(input('choose file to attach, enter -1 to not attach: '))
	if choice != -1:
		attach = files[choice]
	else:
		attach = None
	if input('save to saved.json? (y/n) ').lower() == 'y':
		d = {}
		d['fromU'] = fromU
		d['sub'] = sub
		d['body'] = body
		d['attach'] = attach
		save(d)
	return (fromU, sub, body, attach)


def save(d):
	with open('saved.json', 'w') as file:
		json.dump(d, file)