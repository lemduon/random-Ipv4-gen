from random import *
from time import sleep

strings = [str(randint(100, 200)),
           str(randint(1,100)),
           str(randint(1,100)),
           str(randint(1,100))]

while True:
    print('.'.join(strings))
    sleep(60)
