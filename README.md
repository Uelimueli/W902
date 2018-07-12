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

Erklärung der Funktionsweise von [Ultraschallsensoren](https://www.microsonic.de/de/service/ultraschallsensoren/prinzip.htm "Ultraschallsensor Funktion").


## Sicherheitsaspekte
Die erste Frage die sich bei dieser Konfiguration und Funktion stellt, ist die Umgebung für den Einsatz.
Eine Überwachung kann und wird im privaten, wie auch im Geschäftlichen Bereich genutzt.
Wenn man sich aber die Anforderungen und Standards einer Geschäftlichen Kamera überwachung anschaut, ist dieses Projekt nicht professioniell genug.
Hier sieht man eine Unvollständige Anforderungsliste, die unser Projekt bereits nicht erfüllen würde.

| Anforderungen             | Checkbox                                                                                                  |
| ------------------------- | :-------------------------------------------------------------------------------------------------------- |
| Funktion bei Stromausfall | <ul><li>- [ ] </li></ul>                                                                                  |
| Live Monitoring           | <ul><li>- [ ] </li></ul>                                                                                  |
| Meldung bei Bewegung      | <ul><li>- [x] </li></ul>                                                                                  |
| Live Verschlüsselung      | <ul><li>- [ ] </li></ul>                                                                                  |
| Video Aufzeichnung        | <ul><li>- [ ] </li></ul>                                                                                  |
| Funktionelles Gehäuse     | <ul><li>- [x] Raspy [Gehäuse](https://www.pi-shop.ch/gehause/kamera-gehaeuse "Kamera Gehäuse") </li></ul> |

So ist der Verwendungsort Logischerweise im Privaten Bereich.
Die Kommunikation der 2 Raspberry Pi's läut über das Interne Netzwerk. Die Raspberry Pi erhalten je eine Private IP Adresse.
Als erste Sperre für Angreifer fungiert hier Logischerweise eine konfigurierte Firewall.
Die Übertragung sollte wenn möglich trotzdem verschlüsselt werden, hier eignet sich [TLS](http://www.kryptowissen.de/transport-layer-security-tls.php "TLS Verschlüsselung erklärt").  
Selbstverständlicherweise sollten die Geräte Wöchentliche Updates und Patches erhalten.
Da wir keine öffentlichen IP Adressen verwenden, kann von Ausserhalb des Netzes keine direkte Verbindung hergestellt werden. Um die Geräte trotzdem zu verwalten, könnte man  eine VPN Verbîndung herstellen.
Da wir im Beispiel eine Cloud von einem Externen Anbieter nutzten, müssen wir im in sachen Sicherheit [Vertrauen](https://www.dropbox.com/de/security#datensicherheit "Datensicherheit DropBox").
Diese, für uns nicht kontrollierbare, Variabel könnte aber auch von uns Verwaltet werden. Beispielsweise mit einer eigenen [Cloud](https://owncloud.org/download/ "OwnCloud") auf einem Privaten [Server](https://www.hosttech.ch/server "Hosttech").

## Transfer in die Praxis
Eine Erläuterung weshalb dieses Projekt bestimmt nicht eins zu eins im Geschäftlichen Bereich genutzt werden kann, findet man im Kapitel Sicherheitsaspekte.
Doch neben den Sicherheitsanpassungen sind auch weitere Punkte von Bedeutung, um dieses Equipment anzuwenden.  
Erforderliche Schritte um das ganze nutzen können, werde ich nun auflisten:

### Hardwareanforderungen
Günstigere Alternative für die Rechner
Bewegungsmelder mit grösserer Reichweitenabdeckung  
Überwachungskamera mit passender Auflösung  
USV anschluss oder eigene Batterie

### Sicherheitsaspekte
Private IP Adresse  
Firewall  
TLS Verschlüsselung  
VPN  
Eigene Cloud

### Handling
Gui für die Verwaltung


### Umgebung
Dem Wetter und Licht angepasste Umgebung


### Fremdeinflüsse
Kompatibel mit bereits aktivem Equipment
Datenschutzgesetz
Einbindung in Sicherheitskonzept