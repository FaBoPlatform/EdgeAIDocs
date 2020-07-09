# Servo

## ライブラリ

smbus2をインストール

```
sudo pip3 install smbus2
```

FaBoPWMをインストール

```
git clone https://github.com/FaBoPlatform/FaBoPWM-PCA9685-Python
cd FaBoPWM-PCA9685-Python
sudo pip3 install .
```

## ソース

初期化

```
# coding: utf-8
import Fabo_PCA9685
import time
import pkg_resources
SMBUS='smbus'
for dist in pkg_resources.working_set:
    #print(dist.project_name, dist.version)
    if dist.project_name == 'smbus':
        break
    if dist.project_name == 'smbus2':
        SMBUS='smbus2'
        break
if SMBUS == 'smbus':
    import smbus
elif SMBUS == 'smbus2':
    import smbus2 as smbus

# init
BUSNUM=1
SERVO_HZ=50
INITIAL_VALUE=300
bus = smbus.SMBus(BUSNUM)
PCA9685 = Fabo_PCA9685.PCA9685(bus,INITIAL_VALUE,address=0x60)
PCA9685.set_hz(SERVO_HZ)
```

値を設定

```
# set value
value = 330
channel = 0 # PWM0番目のピンのサーボ
PCA9685.set_channel_value(channel,value)
```