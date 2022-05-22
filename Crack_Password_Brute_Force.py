import random
import time

#courtesy of https://github.com/MustafaTheCoder

def split(word):
    return list(word)

keep_going = True
guess_password = ""
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%&'()*+,-./:;<=>?@[\]^_`{|}~"


password = input("Enter Password: ")
# store starting time
begin = time.time()
  
# program body starts
while keep_going:
    guess_password = random.choices(split(chars), k=len(password))
    print("<============"+ str(guess_password) +"============>")
    
    if guess_password == list(password):
	    print("Cracked Password: " + "".join(guess_password))
	    time.sleep(1)
	    # store end time
	    end = time.time()
	    # total time taken
	    print(f"Total runtime of the program is {end - begin} s")
	    keep_going = False
