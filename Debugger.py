# imports

import os

# variables

while True:
	file = input(">> File Name: ")
	if file and os.path.exists(file):
		if os.path.isfile(file):
			with open(file, 'r') as f:
				content = f.read()
				try:
					exec(content)
				except Exception as Err:
					print(Err)