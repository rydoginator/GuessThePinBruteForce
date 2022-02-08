import requests, time, csv, random, sys

from os import system, name

from time import sleep


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def guess(x):
	zero_x = str(x).zfill(4)
	userdata = {"guess": zero_x}
	try:
		resp = requests.post('https://www.guessthepin.com/prg.php', userdata)
		return str(resp.content).lower().find("confetti")
	except:
		return -2



def main():
	clear()
	with open("common.csv") as csvfile:
		entries = list(csv.reader(csvfile))
		# copy the list so that it can be reused 
		default = entries.copy()
		csvfile.close()	

	while (len(entries) > 0):
		dice = random.randint(0, len(entries) - 1)
		pin = entries.pop(dice)
		res = guess(dice)
		percent = (10000 - len(entries)) / 100
		if (res == -2):
			clear()
			print("Connection refused...", res)
			entries.clear()
			entries = default.copy()
			sleep(0.5)
			clear()
		elif (res == -1):
			print("Brute forcing... {:.2f} %".format(percent), end = "\r")
		else:
			clear()
			print("Found ", pin[0])
			f = open('found.txt','a+')
			f.write(pin[0] + "," + str(10000 - len(entries)) + ",\n")
			f.close()
			entries.clear()
			clear()
			entries = default.copy()			
main()