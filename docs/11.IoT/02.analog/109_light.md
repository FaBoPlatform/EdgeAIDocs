# 109 light

## サンプルコードの動作

FaBo #109 light Brickを使用して光の強さを計測

## サンプルコード使用時の接続

A0にAnalog Brickを接続,GPIO12にLED2を接続します。

![](./../../img/109_Light/109_light.jpg)

## JETSON NANO GPIO40ピン
| ピン番号 |  Jetson.GPIO番号  |  NAME  | ピン番号 |  Jetson.GPIO番号  |  NAME  |
| :---: | :---: |---- | :---: | :---: |---- |
|  1  | - |  3.3V  | 2 | - |  5V  |
|  3  | 2 |  I2C_2_SDA  | 4  | - |  5V  |
|  5  | 3 |  I2C_2_SCL  | 6  | - |  GND  |
|  7  | 4 |  AUDIO_MCLK  | 8 | 14 |  UART_2_TX  |
|  9  | - |  GND  | 10  | 15 |  UART_2_RX  |
|  11  | 17 |  UART_2_RTS  | 12  | 18 |  I2S_4_SCLK  |
|  13  | 27 |  SPI_2_SCK  | 14  | - |  GND  |
|  15 | 22 |  LCD_TE  | 16  | 23 |  SPI_2_CS1  |
|  17  | - |  3.3V  | 18  | 24 |  SPI_2_CS0  |
|  19  | 10 |  SPI_1_MOSI  | 20  | - |  GND  |
|  21  | 9 |  SPI_1_MISO  | 22  | 25 |  SPI_2_MISO  |
|  23  | 11 |  SPI_1_SCK  | 24  | 8 |  SPI_1_CS0  |
|  25  | - |  GND  | 26  | 7 |  SPI_1_CS1  |
|  27  | - |  I2C_1_SDA  | 28  | - |  I2C_1_SCL  |
|  29  | 5 |  CAM_AF_EN  | 30  | - |  GND  |
|  31  | 6 |  GPIO_OZ0  | 32  | 12 |  LCD_BL_PWM  |
|  33  | 13 |  GPIO_PE6  | 34  |  - |  GND  |
|  35  | 19 |  I2S_4_LRCK  | 36  | 16 |  UART_2_CTS  |
|  37  | 26 |  SPI_2_MOSI  | 38  | 20 |  I2S_4_SDIN  |
|  39  | - |  GND  | 40  | 21 |  I2S_4_SDOUT  |

## Brick回路図

![](./../../img/109_Light/109_light_sch.png)

光が当てると数値は、低くなり。光が遮ると数値が高くなります。

<br>


## 準備
SPIとPWMをつかえるようにしましょう。（設定済みの場合は不要です。）

Jetson-IO toolを起動します。

```
$sudo /opt/nvidia/jetson-io/jetson-io.py
```

Pinmux テーブルの設定


![](./../../img/109_Light/JetsonExpansion01.png)

Configure 40-pin expansion headerを選択します。

![](./../../img/109_Light/JetsonExpansion02.png)

PWM０はLED、SPI1は、ADコンバータICと接続するため、

PWM0とSPI１を有効化します。スペースバーで決定。

![](./../../img/109_Light/JetsonExpansion03.png)

Backを選択します。

![](./../../img/109_Light/JetsonExpansion04.png)

Save and reboot to reconfigure pins を選択します。

再起動します。

![](./../../img/109_Light/JetsonExpansion05.png)


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
