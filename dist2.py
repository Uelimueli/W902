# GrovePi + Grove Ultrasonic Ranger
from grovepi import *
# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
import os


ultrasonic_ranger = 4



while True:
 try:
        # Read distance value from Ultrasonic
        d = ultrasonicRead(ultrasonic_ranger)
        print ultrasonicRead(ultrasonic_ranger)
        if d < 150:
                os.system("./mos.sh")

    except TypeError:
        print "Error"
    except IOError:
        print "Error"

