# 129 UltraSound

超音波距離センサー（HC-SR04)

## サンプルコードの動作
0.5秒ごとに即距します。

## サンプルコード使用時の接続
FaBo BLOCKS #129 を#519基板　５、６、２２があるGPIOポートへ接続します。

センサーの動作電圧はDC５.0Vなので＃５１９基板のスライドスイッチを５V側にします。

## サンプルコード

```Python
# FaBo 129 UltraSound ＨＣ－ＳＲ０４
# coding: utf-8
import Jetson.GPIO as GPIO
import time
import sys

#Jetson Nano #519 RJ11
Trig = 5                          
Echo = 6                          
PowerOn = 22

class Sensor():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)             
        GPIO.setup(Trig, GPIO.OUT)         
        GPIO.setup(Echo, GPIO.IN)          
        GPIO.setup(PowerOn, GPIO.OUT)  
        GPIO.output(PowerOn, GPIO.HIGH)

    def getDistance(self):
        GPIO.output(Trig, GPIO.HIGH)
        time.sleep(0.00001)        
        GPIO.output(Trig, GPIO.LOW)

        signaloff=0
        signalon=0

        while GPIO.input(Echo) == 0:
            signaloff = time.time()

        while GPIO.input(Echo) == 1:
            signalon = time.time()

        return (signalon - signaloff) * 17000

sensor = Sensor()

while True:
    try:
        distance = sensor.getDistance()
        print("{:.0f}cm".format(distance))
        time.sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit() 

```
