# W902
Elia Bruno, Michael Gerber
Kamera überwachung mit einem Raspberry Pi 
## Übersicht
1. Vorbereitung
2. Beschreibung
3. Konfiguration
4. Links der Theorie
5. Sicherheitsaspekte
6. Transfer in die Praxis

## Vorbereitung
### Benötigtes Equipment:
* Ultrasonic Sensor - HC-SR04 [Ultrasonic Sensor](https://www.sparkfun.com/products/13959 "Ultrasonic Sensor Link")
* Camera Module V2 [Kamera Modul](https://www.raspberrypi.org/products/camera-module-v2/ "Kamera Modul Link")
* Raspberry Pi [Raspberry Pi](https://www.raspberrypi.org/products/ "Raspberry Pi Link")
### Benötigte Software
* Installiere [Raspbian](https://www.raspberrypi.org/downloads/raspbian/ "Raspbian Download Link")
* Installiere [Python](https://www.python.org/downloads/ "Python Download Link")


## Beschreibung
### Funktionsprinzip
1. Der Raspberry Pi mit dem angeschlossenen Ultraschall Sensor wird bei der zu überwachenden Türe Platziert.
2. Mit dem Python [Skript](https://github.com/Uelimueli/W902) wird eine Meldung ausgegeben wenn eine Distanzveränderung stattfindet.
3. Die Meldung wird per MQTT an den 2ten Raspberry Pi mit der Kamera geleitet.
4. Der Kamera Raspberry Pi schiesst ausgelöst von dem [Skript](https://github.com/Uelimueli/W902) ein Foto von der Türe.
5. Das Foto wird per [Skript](https://github.com/Uelimueli/W902) auf eine Cloud, im Beispiel Dropbox geladen.

### Grafische Darstellung

![Grafik](https://github.com/Uelimueli/W902/blob/master/Grafik.png "Darstellung Grafisch")

## Konfiguration

##Links der Theorie
[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

## Test
| Step | Description                               | Does it work |
| ----:|:-----------------------------------------:| ------------:|
| 1    | Testing connection of the MySQL Database. | Yes |
| 2    |  |   $12 |
| 3    | are neat      |    $1 |

## Evaluation
The work with Vagrant, was my first touch with automatic installation and I learned a lot of new things. I have now the ability to setup new systems with a self created vagrant file.