from random import *
from time import sleep

while True:
    string1 = str(randint(1, 200))
    string2 = str(randint(1,100))
    string3 = str(randint(1,100))
    string4 = str(randint(1,100))
    
    print('.'.join([string1, string2, string3, string4]))
    sleep(30)
