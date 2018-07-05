import os
import sys

from postoffice import PostMan
from reader import *


if __name__ == '__main__':
		
	# Create SMTP Server object
	fromU, sub, body, attach = read()
	postman = PostMan(fromU, sub, body, attach)
	postman.login()

	# Get array of reciepent details	
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
	print("Starting mailing loop, output redirected to logs.txt")
	
	# Redirect output to file
	with open("logs.txt", 'w') as logs_file:
		sys.stdout = logs_file
		print("Redirecting STDOUT to logs file\n\n")
			
		# Number of mails to send
		count_mails = len(people)

		# Send mail to all mail addresses in
		# 'people' array
		for mail_num in range(0,count_mails):

			# Log mail details
			print("Sending mail {} of {}".format(mail_num + 1, count_mails))
			print("To: {}\nCompany: {}".format(people[mail_num]["email"], people[mail_num]["company"]))
			
			# Send Mail
			postman.sendMessage(people[mail_num]["email"], people[mail_num]["company"])

			# Confirm reciept
			print("Sent\n")

	# Quit server
	postman.quit()
