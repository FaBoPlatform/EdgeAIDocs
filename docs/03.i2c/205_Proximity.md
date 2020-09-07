# 205 Proximty


## サンプルコードの動作


## サンプルコード使用時の接続
FaBo #2 を I2C0,I2C1,I2C2のいずれかに接続します。 

![](./../img/211_7Seg/i2cpin.jpg)


## Brick回路図
~画像〜

FaBoのライブラリをインストール
```
git clone https://github.com/FaBoPlatform/FaBoProximity-VCNL4010-Python.git
cd FaBoProximity-VCNL4010-Python
sudo pip3 install .
```


```
# coding: utf-8
import FaBoProximity_VCNL4010
import time
import sys

vcnl4010 = FaBoProximity_VCNL4010.VCNL4010()

try:
    while True:
        p = vcnl4010.readProx()
        a = vcnl4010.readAmbi()
        sys.stdout.write("\rProx=%f, Ambi=%f" % (p,  a))
        sys.stdout.flush()

        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
```

