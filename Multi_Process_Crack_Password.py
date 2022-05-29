import concurrent.futures
import time
import random

#is this the best guess the number machine?

password = input("Enter Password: ")
start = time.perf_counter()

def do_something(name, password):
    keep_going = True
    guess_password = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    print("Running %s\n" %name)
    # program body starts
    while keep_going:
        guess_password = random.choices(list(chars), k=len(password))
        print("<============"+ str(guess_password) +"============>", end = '\r')
        if guess_password == list(password):
            print("Cracked Password: " + "".join(guess_password))
            print(f"{name} has finished execution\n")
            keep_going = False
            break

with concurrent.futures.ProcessPoolExecutor() as executor:
  f1 = executor.submit(do_something, "First Thread", password)
  f2 = executor.submit(do_something, "Second Thread", password)
  f3 = executor.submit(do_something, "Third Thread", password)
  f4 = executor.submit(do_something, "Fourth Thread", password)
  f5 = executor.submit(do_something, "Fifth Thread", password)

#print(DB_password, len(DB_password), 'tries')
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')
