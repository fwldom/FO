from os import *
system("mkdir C:\\Apps\\fwldom-os")
cwd = getcwd()
system(f"xcopy {cwd}\*.* C:\\Apps\\fwldom-os")
system("python \"C:\\Apps\\fwldom-os\\Fwldom os.py\"")