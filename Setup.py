from os import *
system("mkdir C:\\Apps\\fwldom-os")
cwd = getcwd()
system(f"xcopy {cwd}\\Data\\*.* C:\\Apps\\fwldom-os")
system("python \"C:\\Apps\\fwldom-os\\Fwldom os.py\"")