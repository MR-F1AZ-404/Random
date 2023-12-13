import os,platform
os.system('git pull')
Random=platform.architecture()[0]
if Random=="32bit":print("Sorry 32 bit not supported")
elif Random=="64bit":__import__("Random")
