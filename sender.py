from postoffice import PostMan

from reader import *

if __name__ == '__main__':
	fromU, sub, body, attach = read()
	postman = PostMan(fromU, sub, body, attach)
	postman.login()

	for i in get_people('a.csv',10,20):
		pass