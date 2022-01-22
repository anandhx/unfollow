#Importing Modules...
from ast import Break
import random
import time
from instabot import Bot
import os

#Clear the Console Func...
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#define the countdown func...
def delay_counter(delay_time):
    while delay_time:
        mins, secs = divmod(delay_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\u001b[31;1mDelay Time Counter",timer, end="\r\u001b[0m")
        time.sleep(1)
        delay_time -= 1

def countdown(counter_time):
    while counter_time:
        mins, secs = divmod(counter_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\u001b[33;1mDelay Time Counter\u001b[0m\u001b[31;1m",timer, end="\r\u001b[0m")
        time.sleep(1)
        counter_time -= 1        

#Bot Parameters...
bot = Bot(
    unfollow_delay=10,
    follow_delay=10,
    unlike_delay=10,
    max_unfollows_per_day=200,
    )

#Running...
clear()
print("---------------------------------------------------------------------"),time.sleep(0.1)
print('''\u001b[33;1m                                                            
     ___      .__   __.      ___      .__   __.  _______   __    __   __    __  
    /   \     |  \ |  |     /   \     |  \ |  | |       \ |  |  |  | |  |  |  | 
   /  ^  \    |   \|  |    /  ^  \    |   \|  | |  .--.  ||  |__|  | |  |  |  | 
  /  /_\  \   |  . `  |   /  /_\  \   |  . `  | |  |  |  ||   __   | |  |  |  | 
 /  _____  \  |  |\   |  /  _____  \  |  |\   | |  '--'  ||  |  |  | |  `--'  | 
/__/     \__\ |__| \__| /__/     \__\ |__| \__| |_______/ |__|  |__|  \______/ \u001b[0m '''),time.sleep(0.1)
print('                              -MINDFREEZER-🤖'),time.sleep(0.1)
print("---------------------------------------------------------------------"),time.sleep(0.1)

#Input From User...
USERNAME = input("\u001b[32m[+]\u001b[0m Enter Username:-")
PASSWORD = input("\u001b[32m[+]\u001b[0m Enter Password:-")
print("---------------------------------------------------------------------"),time.sleep(0.1)

bot.login(username=USERNAME,password=PASSWORD,use_cookie=False)
clear()

print("---------------------------------------------------------------------"),time.sleep(0.1)
print('''\u001b[33;1m                                                            
     ___      .__   __.      ___      .__   __.  _______   __    __   __    __  
    /   \     |  \ |  |     /   \     |  \ |  | |       \ |  |  |  | |  |  |  | 
   /  ^  \    |   \|  |    /  ^  \    |   \|  | |  .--.  ||  |__|  | |  |  |  | 
  /  /_\  \   |  . `  |   /  /_\  \   |  . `  | |  |  |  ||   __   | |  |  |  | 
 /  _____  \  |  |\   |  /  _____  \  |  |\   | |  '--'  ||  |  |  | |  `--'  | 
/__/     \__\ |__| \__| /__/     \__\ |__| \__| |_______/ |__|  |__|  \______/ \u001b[0m '''),time.sleep(0.1)
print('                              -UNFOLLOW BOT-🤖'),time.sleep(0.1)
print("---------------------------------------------------------------------"),time.sleep(0.1)
print("[1] U N F O L L O W N O N - F O L L O W E R S ")
print("[2] F O L L O W E R S ")
print("---------------------------------------------------------------------"),time.sleep(0.1)

INPUT_USER = input("Choose An Option:-")

if INPUT_USER == "1":
    while True:
        try:
            bot.unfollow_non_followers(n_to_unfollows=30)
            delay_counter(400)
        except KeyboardInterrupt:
            break
    console_clear()
    Option_Menu()
            

if INPUT_USER == "2":
    FISTTARGET = input('Enter Target Username:-')
    while True:
        n = 30
        while n > 0:
            n -= 1
            bot.follow(user_id=FISTTARGET)
            countdown(random.randint(40, 30))
            bot.unfollow(user_id=FISTTARGET)
        countdown(random.randint(600, 700))  #AvoidBlock
            