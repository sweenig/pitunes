#requires piglow & gpiozero already installed
######################################
# begin user customizable parameters #
######################################
ledpin = 16 # specifies the pin the button LED is connected to
blueintensity = 128 #specifies the intensity with which the blue light will shine
sunriseduration = 3 #number of seconds for the sun to stay risen
#####################################
# end user customizable parameters  #
#####################################
import piglow
from gpiozero import LED
from time import sleep
piglow.blue(blueintensity)
piglow.show()
led = LED(ledpin)
led.on()
sleep(sunriseduration)
led.off()
