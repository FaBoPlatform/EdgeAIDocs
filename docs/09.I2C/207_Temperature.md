# 207 Temperature


## サンプルコードの動作
温度を計測して表示します。

## サンプルコード使用時の接続
FaBo #207 を I2C0,I2C1,I2C2のいずれかに接続します。 

![](./../img/211_7Seg/i2cpin.jpg)


## Brick回路図
~画像〜

FaBoのライブラリをインストール

```
git clone https://github.com/FaBoPlatform/FaBoTemperature-ADT7410-Python.git
cd FaBoTemperature-ADT7410-Python
sudo pip3 install .
```
## ソースコード

```
# coding: utf-8

import FaBoTemperature_ADT7410
import time
import sys

adt7410 = FaBoTemperature_ADT7410.ADT7410()

try:
    while True:
        t = adt7410.read()
        sys.stdout.write("\rTemp=%f" % t)
        sys.stdout.flush()

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
```

