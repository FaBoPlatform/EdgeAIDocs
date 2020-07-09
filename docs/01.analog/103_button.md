# 103 Button

GPIOの判定　

```
# coding: utf-8
import Jetson.GPIO as GPIO
import sys

LEDPIN = 4
BUTTONPIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(BUTTONPIN, GPIO.IN)

try:
    while True:
        # ボタン押下判定
        if( GPIO.input(BUTTONPIN)):
            # LED点灯
            GPIO.output(LEDPIN, True)
        else:
            # LED消灯
            GPIO.output(LEDPIN, False)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
```

GPIOの入力待ち

```
# coding: utf-8
import Jetson.GPIO as GPIO
import sys

LEDPIN = 4
BUTTONPIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(BUTTONPIN, GPIO.IN)

try:
    while True:
		GPIO.wait_for_edge(BUTTONPIN, GPIO.FALLING)
		print("Button Pressed!")
		GPIO.output(LEDPIN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LEDPIN, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
```

イベントとして取得

```
# coding: utf-8
import Jetson.GPIO as GPIO
import sys

LEDPIN = 4
BUTTONPIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(BUTTONPIN, GPIO.IN)

# blink LED 
def blink(channel):
    for i in range(5):
        GPIO.output(LEDPIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LEDPIN, GPIO.LOW)
        time.sleep(0.5)

GPIO.add_event_detect(BUTTONPIN, GPIO.FALLING, callback=blink, bouncetime=10)

try:
    while True:
    	print("Loop")
		time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
```