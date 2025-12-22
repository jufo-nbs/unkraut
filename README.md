# Jugend Forscht Unkrautvernichtungsroboter

Wir sind eine Gruppe von 4 Schülern aus HEssen (Deutschland). Wir haben im Rahmen einer Schul-Arbeitsgemeinschaft ein Projekt für den Wettbewerb [Jugend Forscht](https://www.jugend-forscht.de/) erarbeitet. 

## Das Projekt

Wir wollten es mit unserem Roboter ermöglichen, Herbizide und Dünger gezielt einzusetzten. 

Die Hoffnung war, dadurch den Herbizidverbrauch zu reduzieren. 

## Unsere Hardware

Wir verwendeten folgende Produkte: 

<sub>Keine Sponsoren oder sonst irgendwas</sub>

### Für den Raspberry Pi:
* [Raspberry Pi 5 16gb RAM](https://www.berrybase.de/raspberry-pi-5-16gb-ram)
* [Raspberry Pi Active Cooler](https://www.berrybase.de/raspberry-pi-active-cooler-luefter-fuer-raspberry-pi-5)
* [Raspberry Pi AI Camera](https://www.berrybase.de/raspberry-pi-ai-camera)
* [Raspberry Pi 27W Power Supply](https://www.berrybase.de/raspberry-pi-ai-camera)
* [Micro SD Karte](https://www.berrybase.de/sandisk-extreme-pro-microsdxc-a2-uhs-i-u3-v30-200mb-s-speicherkarte-adapter-256gb)

### Motoren und Ansteuerung
* [Arduino Nano](https://www.amazon.de/YELUFT-CH340G-Kompatibel-Arduino-Typ-C-Schnittstelle/dp/B0F5PZXH51)
* [2.2 Ohm 5W Widerstand](https://www.amazon.de/PATIKIL-Widerst%C3%A4nde-Widerstand-Netzadapter-Leiterplatte/dp/B0CS3F67QV)
* [Logic Level Converter](https://www.amazon.de/AZDelivery-TXS0108E-Converter-Arduino-Raspberry/dp/B07N7FFY2Q)
* [Servo-Treiber](https://www.amazon.de/AZDelivery-PCA9685-Servotreiber-Arduino-Raspberry/dp/B072N8G7Y9?th=1)
* [Relais](https://www.amazon.de/AZ822-2C-3DSE-Relais-elektromagnetisch-USpule-120VAC/dp/B01LZZPO4O)

## Schaltplan 

![Schaltplan](./schaltplan.png)

## Rebuild the Projekt

1. Wenn du alle Komponenten hast, installiere Raspbian und Python 3.13 auf dem Raspberry Pi.
2. Installiere diese Python-Erweiterung uaf dem Raspberry Pi:
    * picamera2
3. Lasse [diesen code](/Arduino/main.ino) auf dem Arduino laufen.
4. Verkabele die Komponenten entsprechend des Schaltplanes und schließe die Kamera an den Pi an.
5. Klone das Repository auf denRaspberry Pi.
6. Erstelle dir bei [plantnet](https://my.plantnet.org/) einen Account un einen API-Key. Erstelle dann eine Datei `api_key.py` im Ordner [rpi_drivers](/rpi_drivers) und speichere deinen API-Key in dieser Datei in der Variable `API_KEY` als String.
7. Führe die [main.py](/main.py) auf dem Raspberry Pi aus.
