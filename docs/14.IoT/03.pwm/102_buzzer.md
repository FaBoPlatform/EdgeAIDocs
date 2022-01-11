# 102 buzzer

## サンプルコードの動作
JetsonのGPIOからPWM信号を出力し矩形波ドレミの音階を出力します。

## サンプルコード使用時の接続
FaBo #102 buzzerをGPIO12（32pin）,GPIO13(33pin)
)に接続します。


JetsonからPWM信号を出力します。ハードウェアPWM信号でのピンは決まっておりFaBo519の場合は、PWM0とPWM2が利用可能となっており、以下を設定します。

docker 起動前に

以下を入力し
```
＄sudo /opt/nvidia/jetson-io/jetson-io.py
```

Jetson Expansion Header Toolが起動します。


カーソルキー下を押してConfigure 40-pin expansion headerを選んでエンターキーを押します。


有効にしたいピン（pwm０または、pwm２）をカーソルとスペースキーで有効にします。選択が終わったらBack選んでエンターキーを押します。


Exitを選択してエンターキーで終了します。
<br>

ソースコード
```python
import Jetson.GPIO as GPIO
import time

tempo = 120
onkai = {"C4":261.6, "C4#":277.2, "D4":293.7 ,"D4#":311.1,"E4":329.6,"F4":349.2,"F4#":370.0,"G4":392.0,"G4#":415.3,"A4":440.0,"A4#":466.2,"B4":493.9,"C5":523.3}
notename = ["C4","D4","E4","F4","G4","A4","B4","C5"]
GPIO.setmode(GPIO.BCM)
PIN = 12 #または13
GPIO.setup(PIN, GPIO.OUT)
buzzer = GPIO.PWM(PIN, 261.6)
buzzer.start(50)
print ("Play Start.")

for i in notename: 
    freq = onkai[i]
    print (freq)
    buzzer.ChangeFrequency(freq)
    time.sleep(60/tempo)

buzzer.stop()
print ("Play Stop.")
GPIO.cleanup()
```

