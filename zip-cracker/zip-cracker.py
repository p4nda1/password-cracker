import os

try:
   pass_file = open("password-list.txt", "r")
except:
   print("Need password-list.txt to crack")
   quit()

for password in pass_file:
    password = password.replace("\n","")
    cmd = "unzip -P " + password + " FILE_NAME_HERE "
    print(cmd)

    os.system(cmd)
