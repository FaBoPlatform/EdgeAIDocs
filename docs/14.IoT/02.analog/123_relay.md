# 123 RELAY

#Brickのバージョン

\#123 RELAY REV1.0.10以降

## サンプルコードの動作

FaBo #123 RELAYを使用して１秒ごとにリレーを動作させます。
アクティブハイになります。

## サンプルコード使用時の接続

GPIO４に接続します。 

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

