from logging import exception
import discord
from discord.ext import commands
import os
os.system("title What you do dog?")
import time,ctypes
import discord_rpc
# Here We are trying to get token
print("Getting Token...\n")
try:
    with open("token.skeet") as file: 
        token = file.read()
except FileNotFoundError:   #If there is no file with token
    print("File with token not found")
    wl = input("Input your discord token here: ")
    open("token.skeet","w").write(wl)
    token = open("token.skeet").read()
except PermissionError:
    print("Unable to read file")
print("Token Obtained\n")
print(token[0:8]+"...") # Printing first 8 letters of token :p
time.sleep(0.3)
print("Getting Name\n")
try:
    with open("name.skeet") as file: 
        name = file.read()
except FileNotFoundError:   #If there is no file with token
    print("File with name not found")
    wl = input("Input your name here: ")
    open("name.skeet","w").write(wl)
    name = open("name.skeet").read()
except PermissionError:
    print("Unable to read file")
print("Name Obtained")
print(name+"\n")
PREFIX = "."
bot = commands.Bot(command_prefix=PREFIX, caseinsensitive=True, self_bot=True)
bot.remove_command('help')
pid = os.getpid()
print("\nStarting RPC")
try:
    def ready(current_user):
        print("Connecting...".format(current_user))
        time.sleep(1)
        os.system("cls")
        print("Succesfully Connected!")
        time.sleep(1)
        os.system("cls")
        print("Working!\n")
        os.system("echo DO NOT CLOSE THIS WINDOW IF YOU WANT CUSTOM STATUS ON DISCORD")
        os.system("title RPC hinskiego skita")

    def disconnected(codeno, codemsg):

        print("Disconnected from the RPC".format(
            codeno, codemsg
        ))
        time.sleep(1)
        exit()
    def error(errno, errmsg):
        print("A critical error occured".format(
            errno, errmsg
        ))
    callbacks = {
        'ready': ready,
        'disconnected': disconnected,
        'error': error,
    }
    
    discord_rpc.initialize("926235906963275816", callbacks=callbacks, log=True)     # Discord Developer Portal -> RPC if you cannot understand this (obv if you want)
    discord_rpc.update_presence(**{
        'details': f"登录为 ["+name+"] | "+str(pid)+" ",
        'state': "Get Good Get 游性感",
        'start_timestamp': time.time(),
        'large_image_key': "chskeet",
        'large_image_text': 'nie'
    })
    for i in range(3):      
        discord_rpc.update_connection()     
        time.sleep(1)
        discord_rpc.run_callbacks()
    bot.run(token, bot = False)
except Exception as e:  # If error XD
    print(e)
    time.sleep(3)
    exit()