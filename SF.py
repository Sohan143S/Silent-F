import os, sys
os.system("git pull")
try:
    __import__("Silent").SOHAN_CYBER()
except Exception as e:
    exit(str(e)) 
