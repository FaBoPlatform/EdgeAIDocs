# 105 Vibrator

## Jetson対応バージョン

\#105 Vibrator Rev1.0.9以降のもの

## サンプルコードの動作
FaBo #105 Vibrator Brickを使用して１秒ごとに振動を起こします。

## サンプルコード使用時の接続
LED BrickをGPIO４に接続します。 

<br>

## サンプルコード

```Python

# coding: utf-8
import Jetson.GPIO as GPIO
import time
import sys

LEDPIN = 4

GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup( LEDPIN, GPIO.OUT )

try:
    while True:
        GPIO.output( LEDPIN, True )
        time.sleep( 1.0 )
        GPIO.output( LEDPIN, False )
        time.sleep( 1.0 ) 
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
    
```
