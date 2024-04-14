import subprocess
from dotenv import load_dotenv
from os import system

load_dotenv()

subprocess.run(f"taskkill /f /im msedge.exe")
try:
    system('cls')
except:
    pass

