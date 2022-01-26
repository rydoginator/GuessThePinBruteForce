import requests, time, csv, random

from os import system, name

from time import sleep


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

cursor = 0

with open("common.csv") as csvfile:
	entries = list(csv.reader(csvfile))
	# copy the list so that it can be reused 
	default = entries
	while (len(entries) >= 0):
		#random
		dice = random.randint(0, len(entries))
		guess = entries.pop(dice)
		clear()
		# get how many entries used. default file should be 10k lines
		percent = (10000 - len(entries)) / 100
		print("Brute forcing... {:.2f} %".format(percent))
		zero_x = str(guess[0]).zfill(4)
		userdata = {"guess": zero_x}
		try:
		    resp = requests.post('https://www.guessthepin.com/prg.php', userdata)
		    if (str(resp.content).lower().find("confetti") != -1):
		        print("Found ", zero_x)
		        entries = default
		except: 
		    print("Connection refused...")
		    entries = default