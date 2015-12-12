from gpiozero import LED
from time import sleep
from os import system
import sys
import piglow
#initialize led indicator
red = LED(16)
red.off()
piglow.all(0)
piglow.show()
#function to gradually change the volume
def rampvol(speed = 0.25, start = 0, stop = 100, step = 1):
	vol = start
	while vol != stop:
		vol = vol + step
		system("amixer -q sset PCM,0 " + str(vol) + "%")
		sleep(speed)
#blink all the indicators
red.blink(0.25,0.25,5,1)
red.off()
i = 0
while i <= 5:
	piglow.red(1)
	piglow.show()
	i += 1
	sleep(0.5)
	piglow.red(0)
	piglow.show()
	sleep(0.5)
day = int(time.strftime("%j")) #get the day of the year [0,366]
playlist = ( int(day) + offset ) % 2
if playlist == 0:
	if day > 330: #kiss me baby, it's christmas time
		maxvol = 80
		system("mpg321 --random " + mediapath + "christmas/* &")
	else:
		maxvol = 90
		system("mpg321 --random " + mediapath + "music/* &")
elif playlist == 1:
	maxvol = 100
	system("mpg321 --random " + mediapath + "waves/* &")
else:
	pass
rampvol(0.25,0,maxvol)
sleep(2700)
rampvol(10,maxvol,0,-1)
