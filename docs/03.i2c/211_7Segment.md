# 211 7Segment



## サンプルコードの動作
７セグメントを表示します。

## サンプルコード使用時の接続
FaBo #2 を I2C0,I2C1,I2C2のいずれかに接続します。 

## Brick回路図
~画像〜

FaBoのライブラリをインストール

```
git clone https://github.com/FaBoPlatform/FaBo7Segment-TLC59208-Python.git
cd FaBo7Segment-TLC59208-Python
sudo pip3 install .
```

0~9をカウントアップします。
```
# coding: utf-8
import FaBo7Seg_TLC59208
import time

tlc59208 = FaBo7Seg_TLC59208.TLC59208()

try:
    while True:
        for i in xrange(10):
            tlc59208.showNumber(i)
            time.sleep(0.5)

except KeyboardInterrupt:
    tlc59208.showNumber(10)
```


```
# coding: utf-8
import FaBo7Seg_TLC59208
import time

tlc59208 = FaBo7Seg_TLC59208.TLC59208()

try:
    while True:
        tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PIN_A | FaBo7Seg_TLC59208.LED_PIN_G | FaBo7Seg_TLC59208.LED_PIN_D);
        time.sleep(1)
        for i in xrange(10):
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM5)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM4)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM2)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM1)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM0)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM6)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM5)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM4)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM2)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM1)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM0)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM6)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM5)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_OFF)
            time.sleep(0.05)

            tlc59208.showNumber(i)
            time.sleep(1)
            tlc59208.showDot()
            time.sleep(1)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_OFF)
            time.sleep(1)
except KeyboardInterrupt:
    tlc59208.showPattern(FaBo7Seg_TLC59208.LED_OFF)
```

