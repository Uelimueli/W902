# W902
Elia Bruno, Michael Gerber
Kamera überwachung mit einem Raspberry Pi 
## Übersicht
1. Vorbereitung
2. Beschreibung
3. Konfiguration
4. Theorie und Links
5. Sicherheitsaspekte
6. Transfer in die Praxis

## Vorbereitung
### Benötigtes Equipment:
* Ultrasonic Sensor - HC-SR04 [Ultrasonic Sensor](https://www.sparkfun.com/products/13959 "Ultrasonic Sensor Link")
* Camera Module V2 [Kamera Modul](https://www.raspberrypi.org/products/camera-module-v2/ "Kamera Modul Link")
* 2 Raspberry Pi [Raspberry Pi](https://www.raspberrypi.org/products/ "Raspberry Pi Link")
### Benötigte Software
* Installiere [Raspbian](https://www.raspberrypi.org/downloads/raspbian/ "Raspbian Download Link")
* Installiere [Python](https://www.python.org/downloads/ "Python Download Link")


## Beschreibung
### Funktionsprinzip
1. Der Raspberry Pi mit dem angeschlossenen Ultraschall Sensor wird bei der zu überwachenden Türe Platziert.
2. Mit dem Python [Skript](https://github.com/Uelimueli/W902) wird eine Meldung ausgegeben wenn eine Distanzveränderung stattfindet.
3. Die Meldung wird per MQTT an den 2ten Raspberry Pi mit der Kamera geleitet.
4. Der Kamera Raspberry Pi schiesst, ausgelöst von dem [Skript](https://github.com/Uelimueli/W902), ein Foto von der Türe.
5. Das Foto wird per [Skript](https://github.com/Uelimueli/W902) auf eine Cloud, im Beispiel Dropbox, geladen.

### Grafische Darstellung

![Grafik](https://github.com/Uelimueli/W902/blob/master/Grafik.png "Darstellung Grafisch")

## Konfiguration
x

## Theorie und Links
Erklärung der Funktionsweise von Ultraschallsensoren[I'm an inline-style link with title](https://www.microsonic.de/de/service/ultraschallsensoren/prinzip.htm "Ultraschallsensor Funktion")


## Sicherheitsaspekte
Die erste Frage die sich bei dieser Konfiguration und Funktion stellt, ist die Umgebung für den Einsatz.
Eine Überwachung wird im privaten wie auch im Geschäftlichen Bereich genutzt.
Wenn man sich aber die Anforderungen und Standards einer Geschäftlichen Kamera überwachung anschaut, ist dieses Projekt nicht Professioniell genug.

| Anforderungen             | Checkbox                                          |
| ------------------------- |:-------------------------------------------------:|
| Lückenlose Überwachung    | <ul><li>- [ ] </li></ul> |
| Funktion bei Stromausfall | - [ ]         |
| Live Übertragung          | - [ ]         |
| Meldung bei Bewegung      | 