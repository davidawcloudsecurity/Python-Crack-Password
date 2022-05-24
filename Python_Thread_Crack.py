import logging
import threading
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

def brute_func(keep_going, guess_password, chars, password):
    logging.info("Thread : starting")
    # program body starts
    while keep_going:
        guess_password = random.choices(split(chars), k=len(password))
        print("<============"+ str(guess_password) +"============>")
    
        if guess_password == list(password):
	        print("Cracked Password: " + "".join(guess_password))
	        keep_going = False
	        logging.info("Thread : finishing")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

logging.info("Main    : before creating thread")
x = threading.Thread(target=brute_func, args=(keep_going, guess_password, chars, password,))
logging.info("Main    : before running thread")
x.start()
logging.info("Main    : wait for the thread to finish")
x.join()
logging.info("Main    : all done")

# total time taken
print(f"Total runtime of the program is {timer()-start} s")
	        
