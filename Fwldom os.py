try :
     from colorama import * 
     import random
     from time import *
     from os import *
except:
     print("Error Code 1 : Not Install packages . Installing  packages . Connect To Internet . ")
     system("pip install colorama" or "pip3 install colorama")


#Start Logo
print(Fore.GREEN +"")
system("cls" or "clear")
print("Starting Fwldom OS ... ")
sleep(2)
system("cls" or "clear")
print("Loading ..")
sleep(0.5)
system("cls" or "clear")
print("Loading ...")
sleep(0.5)
system("cls" or "clear")
print("Loading .")
sleep(0.5)
system("cls" or "clear")
print("Loading ..")
sleep(0.5)
system("cls" or "clear")
print("Loading ...")
sleep(0.5)
system("cls" or "clear")
print("Loading ..")
sleep(0.5)
system("cls" or "clear")
print("Loading ...")
sleep(0.5)


system("cls" or "clear")
print("*********")
sleep(0.2)
system("cls" or "clear")
print("F********")
sleep(0.2)
system("cls" or "clear")
print("FW*******")
sleep(0.2)
system("cls" or "clear")
print("FWL******")
sleep(0.2)
system("cls" or "clear")
print("FWLD*****")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM***")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_**")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_O*")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_OS")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_OS")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_OS")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_OS")
sleep(0.5)
system("cls" or "clear")
print("FWLDOM_OS")
sleep(0.5)
system("cls" or "clear")
print("FWLDOM_OS")
sleep(0.5)
system("cls" or "clear")
print(Fore.BLUE +" ██████  ██    ██    ██   ██           ████████        █████       ████████████")
sleep(1)
print(           " ██  f   ██    ██    ██   ██          ██      ██      █     █      ██   ██   ██")
print(           " ██████  ██    ██ w  ██   ██  L       ██   D    ██   █    O  █     ██ M ██   ██")
sleep(1)
print(           " ██      ██    ██    ██   ██          ██       ██     █     █      ██   ██   ██")
print(           " ██      ██    ██    ██   ██          ██     ██        █████       ██   ██   ██")
sleep(2)
print(           " ██       ███████████     ███████      ███████ \n" + Fore.RESET)
print(Fore.CYAN +  " Name App : Fwldom OS ; | App Version : 1.00.00 ; | More : 100 Api .")
sleep(0.5)
print(Fore.GREEN + " Fwldom Hackers . For Woman Life Freedom . Are You Ready ?" + Fore.BLACK)
sleep(0.4)
print(Fore.LIGHTYELLOW_EX +   " WebSite : www.fwldom.rf.gd , GitHub : fwldom , Telegram : @Fwldom1")
UserName = ""
Password = ""
#End Start Logo 
UserName = str(input(Fore.GREEN+" Enter Name User : "))
Password = str(input(f" Enter Password {UserName} : "))
command = ""

multiple_lines = [f"{UserName}",f"{Password}"]
with open("Data.txt", "w") as f:
  f.writelines(multiple_lines)
while command != "exit":
     command = str(input(" FO>> : "))
     command = command.lower().replace(" " , "")
     if command == "smsbomb":
          system("python FWLDOM_BOMB.py" or "python3 FWLDOM_BOMB.py")
     elif command == "":
         print(" Please Type Command .")
         continue
     elif command[0:4] == "ping":
          command += " "
          system(f"ping {command[4:-1]}")
          continue
     elif command =="help":
          print(
                '''
                ============================================================
                Command      &    about
                ping              ping google.com : Get a ping from the site .
                help              Help fwldom os 
                ============================================================
                Name Apps         &    about 
                smsbomb           SMS BOMBER Iran 94 Api High Speed .
                calculator        calculator / ** * - + 


'''
          )
          continue

     elif command == "calculator":
          system("python Calculator.py" or "python3 Calculator.py")
          continue
     elif command == "fogg":
          system("pip install turtle" or "pip3 install turtle")
          system("python FOGG.py" or "python3 FOGG.py")
          system("cls" or "clear")
          continue


     else:
          system(command)
