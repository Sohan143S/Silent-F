import os, sys
os.system("git pull")
try:
    __import__("Silentx").SOHAN_CYBER()
except Exception as e:
    exit(str(e)) 
