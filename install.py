import os, time

os.system('apt-get install python')
os.system('apt-get install pip')

try:
	import colorama
	from colorama import Fore,Back

except ImportError:
	os.system("sudo pip install colorama")

os.system('clear')

uid = os.getuid()

f = Fore
r = f.RED
g = f.GREEN
m = f.MAGENTA
c = f.CYAN
y = f.YELLOW

print(r+"""
  _    _                _____   _            _   
 | |  (_)_ _ _  ___ __ |_   _| | |   ___  __| |__
 | |__| | ' \ || \ \ /   | |   | |__/ _ \/ _| / /
 |____|_|_||_\_,_/_\_\   |_|   |____\___/\__|_\_\
                                                                                                                                                                                                            
 Linux Terminal Locker By: AL104 | Anikin Luke
""")


print(f"{c}By: Anikin Luke")
time.sleep(1)
print(f"{m} Loading...")
time.sleep(5)

if(uid == 0):
	pass
else:
	print("Error! Run it as root!")
	time.sleep(2)

while True:
	if(uid == 0):
		pass
	else:
		print("Error! Run it as root!")
		time.sleep(2)
		break

	print(y+"Enter the password you want for lock.")
	ui = input("Password: ")
	ui2 = input("ReType Password: ")
	
	if(ui == ui2):
		print(g+"loading..")
		time.sleep(.2)
		print('creating...')
		o = open('lock.py', 'a')
		pload = """
import os, time
os.system('clear')
try:
	import colorama
	from colorama import Fore
except ImportError:
	print("colorama or pip is not installed!!")
	print('auto installing colorama or pip')
	time.sleep(2)
	os.system('apt-get install pip3')
	os.system('pip3 install colorama')
paz = 'ptestp'
f = Fore
r = f.RED
g = f.GREEN
c = f.CYAN
b = f.BLUE
y = f.YELLOW
while True:
	try:
		print(c+b+"Enter password to proceed!")
		ui = input(g+"AL104~: ")
		if(ui == paz):
			print(g+"Nice! Welcome Back!!")
			time.sleep(2)
			os.system("clear")
			break
		else:
			print("ERROR!! wrong password!!")
			time.sleep(.8)
			os.system('clear')
	except KeyboardInterrupt:
		print(r+"Error cannot be bypass!!")
		
		try:
			time.sleep(3)
			os.system("clear")
		except KeyboardInterrupt:
			for i in range (50):
				try:
					time.sleep(.1)
					print("INTRUDER!! GO AWAY SCRIPT KIDDIE!!")
				except KeyboardInterrupt:
					print("LOL YOU WISH YOU CAN!!")
			"""
		payload = pload.replace('ptestp', ui2)
		o.write(payload)
		print("Installing..pls wait")
		os.system('sudo echo python3 /etc/lock.py >> /etc/bash.bashrc')
		os.system('sudo echo python3 /etc/lock.py >> /etc/zsh/zshrc')
		time.sleep(3)
		os.system('sudo mv lock.py /etc')

		print("\n installation done! pls restart termux!")
		print('Important Note! Do not delete the file name lock.py \n')
		print(f"NOTE! REMEMBER YOUR PASSWORD IS >> '{ui2}' << ")

		break

	else:
		print("\nReTyped Password not match in Password\nTRY AGAIN!\n\n")