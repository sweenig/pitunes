from gpiozero import Button
from gpiozero import LED
from time import sleep
from os import system
import sys
import piglow
#initialize led indicator
red = LED(16) #choose which pin to connect the button led to
red.off()
piglow.all(0)
piglow.show()
#initialize button (silly workaround due to a weird bug in gpiozero; written by nuttall
button = None
while not button:
  try:
    button = Button(3)
  except:
    pass
#main callback function for button
def playnap(offset = 0, mediapath = "/home/pi/"):
	#blink all the indicators
    red.blink(0.25,0.25,5,1)
    red.off()
    i = 0
    while i <= 5:
      piglow.red(1)
      piglow.show()
      i += 1
      piglow.red(0)
      piglow.show()
      sleep(1)
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
	sys.exit("Finished playing naptime music")
def rampvol(speed = 0.25, start = 0, stop = 100, step = 1):
  vol = start
  while vol != stop:
    vol = vol + step
    system("amixer -q sset PCM,0 " + str(vol) + "%")
    sleep(speed)
#main program execution
try:
	button.when_pressed = playnap() #what to do when/if the button is pressed
	pause(10800) #have a three hour window during which the button could be pressed
except:
  pass
