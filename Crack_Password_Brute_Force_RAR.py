import rarfile
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from timeit import default_timer as timer

def split(word):
  return list(word)

def sendSMTP():
  # Email details
  sender_email = "foabdavid@gmail.com"
  receiver_email = "foabdavid@gmail.com"
  password = "wsnixqymnluwplrf"
  subject = "RAR open"
  message = "This is a test email from Python"

  # Create a message object
  msg = MIMEMultipart()
  msg['From'] = sender_email
  msg['To'] = receiver_email
  msg['Subject'] = subject

  # Add message to email
  msg.attach(MIMEText(message, 'plain'))

  # Connect to SMTP server and send email
  with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")

keep_going = True
guess_password = ""
length = 3
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%&'()*+,-./:;<=>?@[]^_`{|}~"
chars1 = "321"

global DB_password
DB_password = []

# Replace 'file.rar' with the name of your RAR file
file_name = 'test.rar'

# Create a RarFile object
rar_file = rarfile.RarFile(file_name)
#password1 = rar_file.getinfo(rar_file.namelist()[0]).CRC

start = timer()

# Function to convert list to string
def listToString(s):
  # initialize an empty string
  str1 = ""
  # traverse in the string
  for ele in s:
    str1 += ele
  # return string
  return str1

# Set the password for the RAR file
while keep_going:
  try:
    guess_password = random.choices(split(chars), k=length)
    rar_file.setpassword(listToString(guess_password))
    rar_file.extractall()
    print("Cracked Password: " + "".join(guess_password))
    print(len(DB_password), ' tries')
    # total time taken
    print(f"Total runtime of the program is {timer()-start} s")
    sendSMTP()
    keep_going = False
  except:
    DB_password.append("".join(guess_password))
    #print(f"Incorrect password:{guess_password}")

# Close the RAR file
rar_file.close()
