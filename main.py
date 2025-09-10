#import string patterns
import re

#Reads the one message in the message in the file and gets the message, where choice one goes, where choice 2 goes
def read_msg(message):
    #Open the file
    with open("messages.ook", "r") as file:
        #Get the correct message
        message = file.read().split(f"%msg{message}%")[1].strip()
        #If it has any options
        try:
            options = message.split("1)")[1].split("\n")
            #If the player only has 1 option
            if len(options) > 1:
                return [message, options[0].split("%")[1], options[1].split("%")[1]]
            else:
                return [message, options[0].split("%")[1], options[0].split("%")[1]]
        except:
            #end the sim
            return [message, "break", "break"]

#Set what message to read
choice = 0
while True:
    #Read the message and get the option destinations
    buf = read_msg(choice)
    
    #Get user input of visual message
    i = input(f"{re.sub(r'%..%', '', re.sub(r'%.%', '', buf[0]))}\n")

    #Repeat with new message or end sim
    if buf[1] == "break":
        break
    if i == "1":
        choice = buf[1]
    else:
        choice = buf[2]

