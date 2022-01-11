# 110 Tilt

FaBo #110 Tilt Brickを使用して傾斜を検知します。

GPIO４にLED2を接続し、GPIO5にTiltを接続します

傾斜を検知するとLEDが光ります。

※プルアップ抵抗は、1KΩが付いているもをご使用ください。

```Python
import RPi.GPIO as GPIO
import sys

LED_PIN = 4
TILT_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(TILT_PIN, GPIO.IN)

try:
    while True:
        if(GPIO.input(TILT_PIN)):
            GPIO.output(LED_PIN, True)
        else:
            GPIO.output(LED_PIN, False)

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
```
