# 203 Color

## サンプルコードの動作
赤、緑、青の強さを測ります。

## サンプルコード使用時の接続
FaBo #203 ColorをI2C0,I2C1,I2C2のいずれかに接続します。 

## Brick回路図
~画像〜

FaBoのライブラリをインストール
```
git clone https://github.com/FaBoPlatform/FaBoColor-S11059-Python.git
cd FaBoColor-S11059-Python
sudo pip3 install .
```

ソースコード
```
# coding: utf-8
import FaBoColor_S11059
import time
import sys

s11059 = FaBoColor_S11059.S11059()

try:
    while True:
        c = s11059.read()
        sys.stdout.write("\rr=%f, g=%f, b=%f, ir=%f" % (c['r'],  c['g'], c['b'], c['ir']))
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()
```

