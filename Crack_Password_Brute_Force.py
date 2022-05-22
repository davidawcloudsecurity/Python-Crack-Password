import random
from timeit import default_timer as timer

#courtesy of https://github.com/MustafaTheCoder

def split(word):
    return list(word)

keep_going = True
guess_password = ""
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%&'()*+,-./:;<=>?@[\]^_`{|}~"


password = input("Enter Password: ")
# store starting time
start = timer()
  
# program body starts
while keep_going:
    guess_password = random.choices(split(chars), k=len(password))
    print("<============"+ str(guess_password) +"============>")
    
    if guess_password == list(password):
	    print("Cracked Password: " + "".join(guess_password))
	    # total time taken
	    print(f"Total runtime of the program is {timer()-start} s")
	    keep_going = False
