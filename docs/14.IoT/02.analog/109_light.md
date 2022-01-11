# 109 light

## サンプルコードの動作

FaBo #109 light Brickを使用して光の強さを計測

## サンプルコード使用時の接続

A0にAnalog Brickを接続,GPIO12にLED2を接続します。

光が当てると数値は、低くなり。光が遮ると数値が高くなります。

<br>


## 準備
SPIとPWMを使えるようにしましょう。（設定済みの場合は不要です。）

Jetson-IO toolを起動します。

```
$sudo /opt/nvidia/jetson-io/jetson-io.py
```

Pinmux テーブルの設定


Configure 40-pin expansion headerを選択します。

PWM０はLED、SPI0は、ADコンバータICと接続するため、

PWM0とSPI0を有効化します。スペースバーで決定。

Backを選択します。

Save and reboot to reconfigure pins を選択します。

再起動します。


pip3がインストールされていない場合は、
```
$sudo apt-get install python3-pip
```

pythonでSPIをつかうためのspidevをインストールします。

```
$pip3 install spidev
```

SPIdevの使い方。

https://pypi.org/project/spidev/

<br>

## サンプルコード

```python
# coding: utf-8
import Jetson.GPIO as GPIO
import spidev
import time
import sys

# A0コネクタにLightを接続
LIGHTPIN = 0

# GPIO12コネクタにLEDを接続
LEDPIN = 12

# GPIOポートを設定
GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup( LEDPIN, GPIO.OUT )

def readadc(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# PWM/100Hzに設定
LED = GPIO.PWM(LEDPIN, 100)

# 初期化
LED.start(0)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000

try:
    while True:
        ambient = readadc(LIGHTPIN)
        sys.stdout.write("\rambient = %f" % (ambient))
        sys.stdout.flush()
        value = arduino_map(ambient, 0, 1023, 0, 100)
        LED.ChangeDutyCycle(value)
        time.sleep( 0.01 )
except KeyboardInterrupt:
    LED.stop()
    GPIO.cleanup()
    spi.close()
    sys.exit(0)
```
