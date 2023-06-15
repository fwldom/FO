#Input Number
f = "15"
while f != "exit":
     number = 0
     Number1 = int(input("Enter Number 1 "))
     mda = str(input("Enter  / * ** - + % "))
     Number2 = int(input("Enter Number 2 "))
     #end Input Number
     #/ * ** + - %
     if(mda == "*"):
          number = Number1 * Number2
          print(number)
     if(mda == "**"):
          number = Number1 ** Number2
          print(number)
     if(mda == "-"):
          number = Number1 - Number2
          print(number)
     if(mda == "+"):
          number = Number1 + Number2
          print(number)
     if(mda == "/"):
          number = Number1 / Number2
          print(number)
     if(mda == "%"):
          number = Number1 % Number2
          print(number)
#end / * ** + - %
f = input("Try Again : ")
#for freedom
#mahsa_amini