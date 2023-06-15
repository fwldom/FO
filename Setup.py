from os import *
system("mkdir C:\\Apps\\fwldom-os")
system("mkdir C:\\Apps\\fwldom-os\\Tools")

cwd = getcwd()
system(f"xcopy {cwd}\\Data\\*.* C:\\Apps\\fwldom-os")
system("python \"C:\\Apps\\fwldom-os\\Fwldom os.py\"")