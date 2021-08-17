import os
import hashlib

input_hash = input("Enter md5 hash: ")

try:
   pass_file = open("password-list.txt", "r")
except:
   print("Need password-list.txt to crack")
   quit()

for password in pass_file:
   password = password.replace("\n","")
   enc = password.encode('utf-8')
   digest = hashlib.md5(enc.strip()).hexdigest()

   print("password " + password + " = " + digest)

   if input_hash == digest:
       print("Password found ---> " + password)
       break
