import random
from timeit import default_timer as timer
#uses list to crack
#courtesy of https://github.com/MustafaTheCoder

def split(word):
    return list(word)

keep_going = True
guess_password = ""
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%&'()*+,-./:;<=>?@[\]^_`{|}~"

global DB_password
DB_password = []
password = input("Enter Password: ")
# store starting time
start = timer()
  
# program body starts
while keep_going:
    guess_password = random.choices(split(chars), k=len(password))
    print("<============"+ str(guess_password) +"============>")
    if "".join(guess_password) not in DB_password:
        DB_password.append("".join(guess_password))
        if password in DB_password:
            print("Cracked Password: " + "".join(guess_password))  
            print(len(DB_password), ' tries')
            # total time taken
            print(f"Total runtime of the program is {timer()-start} s")
            keep_going = False
