'''
This program does:
_ generate a 10 characters password 
_ contain small & capital letters and numbers
_ store it in a file (passwords.txt) with its date 
'''
import random 
from datetime import datetime as DT
import os 
import subprocess
import re 
import string 

def generatePassword():
    charactersSet = set(string.ascii_letters+ string.digits)
    charactersSet.update(list("!@#$%&"))
    randomChoicesList= random.choices(list(charactersSet) , k= 10)
    randomPassword = ''.join(randomChoicesList)
    return randomPassword

def checkPassword(s):
    '''
    create a regex that check for using lookahead regex:
    1.capital letters
    2.small letters
    3.digits 
    4.symbols
    '''
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%&]).{10}$"
    pattern = re.compile(regex)
    # match = re.search(pattern=pattern, string=s)
    #better to use match 
    matches = pattern.match(s)
    print('Valid' if matches else 'NotValid')
    return bool(matches)

def trackTime():
    nowMoment = DT.now()
    return DT.ctime(nowMoment)

def savePassword(password:str):
    '''
    checks first if the file exists:
    _exists-> open it 
    _ doesn't exist-> create it 
    '''
    fileName = 'Passwords.txt'
    command = f'notepad.exe {fileName}'
    time = trackTime()

    if not os.path.exists(fileName):
        with open(fileName , "w")as f:
            f.write(f"{password} -> {time}")
            subprocess.Popen(command, shell=True)
    else:
        with open(fileName , "a")as f :
            f.writelines(f"\n{password} -> {time}")
            subprocess.Popen(command , shell= True)

if __name__ == '__main__':
    randomPassword = generatePassword()
    if checkPassword(randomPassword):
        savePassword(randomPassword)
    else:
        print('Generated Password NotValid, Try again!')  