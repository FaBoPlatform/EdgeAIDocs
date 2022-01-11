# 304 USBserial

![](./../img/304_usbserial/usbserial304.jpg)

## サンプルコードの動作
FaBo USB Serialを使いUARTでシリアルで通信いたします。

## サンプルコード使用時の接続
FaBo #304 USB serial を SERIALに接続します。

※注意　#519 Rev1.0.14では#519への信号レベルは3.3Vになります。ジャンパーを3.3Vにセットしてください。#519 Rev1.0.15以降では、信号レベルは5Vとなります。ジャンパーを5Vにセットしてください。
USBシリアルからは＃519へは、給電をしないでください。POWERジャンパピンをはずします。
また、#519 Rev1.0.14以降では、デフォルトでは、SERIALピンのVCC（５V）からは給電されません。

## インストール（Dockerの場合）

dockerの場合は、jupyter labから以下を実行します。

```
!pip3 install pyserial
```

## インストール（Dockerでない場合）

```
$pip3 install pyserial
```

```
$sudo chmod 666 /dev/ttyTHS1
```

## サンプルコード

```Python

#１００文字を入力して送信して表示する。QWERT入力確認
import serial

# /dev/ttyTHS1でボーレート115200、パリティビットなしで設定
ser = serial.Serial("/dev/ttyTHS1", baudrate=115200 ,parity=serial.PARITY_NONE)

# ノイズデータがある場合があるのでバッファをクリアする
ser.reset_input_buffer()

ser.write(b"INPUT CHAR.\r\n")

# 受け取ったデータもバイナリ形式
# 引数は受け取る文字数
for w in range(100):
    recv_data = ser.read(1)
    ser.write(recv_data)

ser.write(b"TEST END.\r\n")

ser.close()
```
