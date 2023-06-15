from os import *
from time import *
IsFile = path.isfile("C:\\Apps\\fwldom-os\\Fwldom os.py")
if IsFile == True:
    print(IsFile)
    sleep(5)
    chdir("C:/Apps/fwldom-os/")
    system("python \"Fwldom os.py\"")
if IsFile == False:
    print(IsFile)
    sleep(5)
    system("mkdir C:\\Apps\\fwldom-os")
    system("mkdir C:\\Apps\\fwldom-os\\Tools")
    cwd = getcwd()
    system(f"xcopy {cwd}\\Data\\*.* C:\\Apps\\fwldom-os")
    system("python \"C:\\Apps\\fwldom-os\\Fwldom os.py\"")
