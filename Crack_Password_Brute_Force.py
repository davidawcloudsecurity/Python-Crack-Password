import random
import string

#Courtesy of https://github.com/MustafaTheCoder

def split(word):
    return list(word)

keep_going = True
guess_password = ""
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%&'()*+,-./:;<=>?@[\]^_`{|}~"

password = input("Enter Password: ")

while keep_going:
    guess_password = random.choices(split(chars), k=len(password))
    print("<============"+ str(guess_password) +"============>")
    
    if guess_password == list(password):
	    print("Cracked Password: " + "".join(guess_password))
	    keep_going = False
