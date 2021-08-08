from time import sleep
from os import name , system
from datetime import datetime
from subprocess import Popen

proc = Popen('py AutoCal.py')


while 1:
    t = datetime.now().time().replace(microsecond = 0)
    if str(t) == '00:00:00' and name == 'nt':
        system('cls')
        proc.terminate()
        sleep(5)
        proc = Popen('py AutoCal.py')
    elif str(t) == '00:00:00' and name != 'nt':
        system('clear')
        proc.terminate()
        sleep(5)
        proc = Popen('py AutoCal.py')