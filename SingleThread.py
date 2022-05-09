#Single-Threaded
from tkinter.font import names
import cumtime
import random
import time
cumtime.register('cum')

cum.begin('t1')
time.sleep(1.0)
#Program Below

# Some lists with our favorite characters
nameSingle = ['Master Shake', 'Meatwad', 'Frylock', 'Carl', 'Early', 'Rusty', 'Sheriff', 'Granny', 'Lil', 'Rick', 'Morty', 'Jerry', 'Summer', 'Beth' ]

for x in range (len(nameSingle)):
    print(nameSingle[x])
    time.sleep(random.randint(0, 10))

#Program Above

cum.end()

print(cum)