import os

from postoffice import PostMan

from reader import *

if __name__ == '__main__':
	fromU, sub, body, attach = read()
	postman = PostMan(fromU, sub, body, attach)
	postman.login()
	csv_files = filter_files(get_files(),"\\.csv")
	if len(csv_files) == 0:
		print("No clean file found. Calling the janitor...")
		os.system("Rscript janitor.R > /dev/null 2>&1")
		csv_files = filter_files(get_files(), "\\.csv")
	for i in range(len(csv_files)):
		print(i,'. ',csv_files[i])
	choice = -1
	while choice not in range(len(csv_files)):
		choice = int(input('Choose a csv file to read from :'))
	i = input("send from :")
	j = input("to :")
	people = get_people(csv_files[choice],i,j)
	for i in people:
		postman.sendMessage(i["email"],i["company"])

