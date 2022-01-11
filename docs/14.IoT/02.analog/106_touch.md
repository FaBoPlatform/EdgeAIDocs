# 106 touch

## サンプルコードの動作

FaBo #104 LED Brickを使用してアナログ値を計測

## サンプルコード使用時の接続

GPIO12にLED Brickを接続、A0にAnalog Brickを接続します。

感圧センサーの状態により数値が変化します。

## 準備

JetPack4.6の環境でSPIを使用するには、docker起動前に、以下を実行します。

```Bash

$modprobe spidev

```

## サンプルコード

```Python

# coding: utf-8
import Jetson.GPIO as GPIO
import spidev
import time
import sys

# A0コネクタにAngleを接続
ANGLEPIN = 0

# GPIO12コネクタにLEDを接続
LEDPIN = 12

#######################################################################
def readadc(channel):
    """
    Analog Data Converterの値を読み込む
    @channel チャンネル番号
    """
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

#######################################################################
def map(x, in_min, in_max, out_min, out_max):
    """
    map関数
    @x 変換したい値
    @in_min 変換前の最小値
    @in_max 変換前の最大値
    @out_min 変換後の最小
    @out_max 変換後の最大値
    @return 変換された値
    """
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# GPIOポートを設定
GPIO.setmode( GPIO.BCM )
GPIO.setup( LEDPIN, GPIO.OUT )

# PWM/100Hzに設定
LED = GPIO.PWM(LEDPIN, 100)

# 初期化
LED.start(0)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000

try:
    while True:
        data = readadc(ANGLEPIN)
        print("adc : {:8} ".format(data))
        value = map(data, 0, 1023, 0, 100)
        LED.ChangeDutyCycle(value)
        time.sleep( 0.01 )
except KeyboardInterrupt:
    LED.stop()
    GPIO.cleanup()
    spi.close()
    sys.exit(0)

```

