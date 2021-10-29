## Jetson.GPIO API

Jetson GPIOライブラリは、RPi.GPIOライブラリによって提供されるすべてのパブリックAPIを提供します。以下では、各APIの使用について説明します。

1.ライブラリのインポート

Jetson.GPIOモジュールをインポートするには、以下を使用します。

```
import Jetson.GPIO as GPIO
```

Jetson.GPIOをGPIOとしてインポートする
これにより、アプリケーションの残りの部分でモジュールをGPIOと呼ぶことができます。モジュールは、RPiライブラリを使用する既存のコードに対して、Jetson.GPIOの代わりにRPi.GPIOという名前を使用してインポートすることもできます。

<br>

2. ピン番号

Jetson GPIOライブラリは、I / Oピンに番号を付ける4つの方法を提供します。最初の2つは、RPi.GPIOライブラリによって提供されるモードに対応しています。つまり、40ピンのGPIOヘッダーのピン番号とBroadcom SoCのGPIO番号をそれぞれ参照するBOARDとBCMです。残りの2つのモード、CVMおよびTEGRA_SOCは、CVM / CVBコネクタおよびTegra SoCの信号名にそれぞれ対応する番号の代わりに文字列を使用します。

使用しているモードを指定するには（必須）、次の関数呼び出しを使用します。

```
GPIO.setmode(GPIO.BOARD)
```

```
GPIO.setmode(GPIO.BCM)
```

```
GPIO.setmode(GPIO.CVM)
```

```
GPIO.setmode(GPIO.TEGRA_SOC)
```

設定されているモードを確認するには、次を呼び出します。

```
mode = GPIO.getmode()
```

モードは、GPIO.BOARD、GPIO.BCM、GPIO.CVM、GPIO.TEGRA_SOC、またはNoneのいずれかである必要があります。

3. 警告

使用しようとしているGPIOが、現在のアプリケーションの外部で既に使用されている可能性があります。このような状況では、使用されているGPIOがデフォルトの方向（入力）以外に設定されている場合、Jetson GPIOライブラリが警告を表示します。また、モードとチャネルを設定する前にクリーンアップしようとすると、警告が表示されます。警告を無効にするには、次を呼び出します。

```
GPIO.setwarnings(False)
```

4. チャンネルセットアップ

GPIOチャネルは、入力または出力として使用する前にセットアップする必要があります。チャネルを入力として構成するには、次を呼び出します。

（チャネルは上記のピン番号付けモードに基づいています）

```
GPIO.setup(channel, GPIO.IN)
```

チャネルを出力として設定するには、次を呼び出します。

```
GPIO.setup(channel, GPIO.OUT)
```

出力チャネルの初期値を指定することもできます。

```
GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
```

チャネルを出力として設定する場合、一度に複数のチャネルを設定することもできます。

＃必要なだけチャネルを追加します。タプルを使用することもできます：（18,12,13）

```
channels = [18, 12, 13]
GPIO.setup(channels, GPIO.OUT)
```

5. 入力

チャネルの値を読み取るには、以下を使用します。

```
GPIO.input(channel)
```

これにより、GPIO.LOWまたはGPIO.HIGHが返されます。


6. 出力

出力として構成されたピンの値を設定するには、以下を使用します。

```
GPIO.output(channel, state)
```

ここで、stateはGPIO.LOWまたはGPIO.HIGHです。

チャネルのリストまたはタプルに出力することもできます。

```
channels = [18, 12, 13] # or use tuples
GPIO.output(channels, GPIO.HIGH) # or GPIO.LOW
# set first channel to HIGH and rest to LOW
GPIO.output(channel, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
```

7. クリーンアップ

プログラムの最後に、すべてのピンがデフォルト状態に設定されるようにチャネルをクリーンアップすることをお勧めします。使用されているすべてのチャネルをクリーンアップするには、次を呼び出します。


```
GPIO.cleanup()
```

すべてのチャネルをクリーンアップしたくない場合は、個々のチャネルまたはチャネルのリストまたはタプルをクリーンアップすることもできます。


```
GPIO.cleanup(chan1) # cleanup only chan1
GPIO.cleanup([chan1, chan2]) # cleanup only chan1 and chan2
GPIO.cleanup((chan1, chan2))  # does the same operation 
as previous statement
```

8. Jetsonボード情報とライブラリバージョン

Jetsonモジュールに関する情報を取得するには、以下を使用/読み取りします。

```
GPIO.JETSON_INFO
```

これにより、Python辞書に次のキーが提供されます：P1_REVISION、RAM、REVISION、TYPE、MANUFACTURERおよびPROCESSOR。整数であるP1_REVISIONを除いて、ディクショナリ内のすべての値は文字列です。

ライブラリのバージョンに関する情報を取得するには、以下を使用/読み取りします。

GPIO.VERSION
これにより、X.Y.Zバージョン形式の文字列が提供されます。


9. 割り込み

ライブラリは、ビジーポーリング以外に、入力イベントを監視する3つの追加方法を提供します。

```
The wait_for_edge() function
```

この関数は、指定されたエッジが検出されるまで、呼び出しスレッドをブロックします。この関数は次のように呼び出すことができます。

2番目のパラメーターは、検出するエッジを指定し、GPIO.RISING、GPIO.FALLING、またはGPIO.BOTHにすることができます。待機を指定した時間だけに制限したい場合は、オプションでタイムアウトを設定できます。


### タイムアウトはミリ秒単位
GPIO.wait_for_edge（チャネル、GPIO.RISING、タイムアウト= 500）
この関数は、エッジが検出されたチャネル、またはタイムアウトが発生した場合はNoneを返します。

```
event_detected（）function
```

この関数を使用して、最後の呼び出し以降にイベントが発生したかどうかを定期的に確認できます。この関数は、次のように設定して呼び出すことができます。

### チャネルの立ち上がりエッジ検出を設定
GPIO.add_event_detect（チャネル、GPIO.RISING）
run_other_code（）
GPIO.event_detected（channel）の場合：
    do_something（）
以前と同様に、GPIO.RISING、GPIO.FALLING、またはGPIO.BOTHのイベントを検出できます。

エッジが検出されたときに実行されるコールバック関数

この機能を使用して、コールバック関数の2番目のスレッドを実行できます。したがって、コールバック関数は、エッジに応答してメインプログラムと同時に実行できます。この機能は次のように使用できます。


### コールバック関数を定義する

```
def callback_fn(channel):
    print("Callback called from channel %s" % channel)
```

### 立ち上がりエッジ検出を追加する

```
GPIO.add_event_detect(channel, GPIO.RISING, callback=callback_fn)
More than one callback can also be added if required as follows:

def callback_one(channel):
    print("First Callback")

def callback_two(channel):
    print("Second Callback")

GPIO.add_event_detect(channel, GPIO.RISING)
GPIO.add_event_callback(channel, callback_one)
GPIO.add_event_callback(channel, callback_two)
```

この場合の2つのコールバックは、すべてのコールバック関数を実行するスレッドしか存在しないため、同時にではなく順次実行されます。

複数のイベントを単一のイベントに折りたたんでコールバック関数を複数回呼び出すのを防ぐために、デバウンス時間をオプションで設定できます。


### ミリ秒単位で設定されたバウンス時間

```
GPIO.add_event_detect(channel, GPIO.RISING, callback=callback_fn,
bouncetime=200)
```

エッジ検出が不要になった場合は、次のように削除できます。

```
GPIO.remove_event_detect(channel)
```

10. GPIOチャネルの機能を確認する

この機能により、提供されているGPIOチャネルの機能を確認できます。

```
GPIO.gpio_function(channel)
```

関数は、GPIO.INまたはGPIO.OUTを返します。


11. PWM

PWMチャネルの使用方法の詳細については、samples / simple_pwm.pyを参照してください。

Jetson.GPIOライブラリは、ハードウェアPWMコントローラーが接続されたピンでのみPWMをサポートします。 RPi.GPIOライブラリとは異なり、Jetson.GPIOライブラリはソフトウェアでエミュレートされたPWMを実装していません。 Jetson Nanoは2つのPWMチャネルをサポートし、Jetson AGX Xavierは3つのPWMチャネルをサポートします。 Jetson TX1およびTX2は、PWMチャネルをサポートしていません。

システムpinmuxは、ハードウェアPWMコントローラーを関連するピンに接続するように構成する必要があります。 pinmuxが構成されていない場合、PWM信号はピンに到達しません Jetson.GPIOライブラリは、これを実現するためにpinmux構成を動的に変更しません。 pinmuxの構成方法の詳細については、L4Tのドキュメントを参照してください。

<br>

## L4Tドキュメントの入手

L4Tのドキュメントは次の場所にあります。

Jetsonダウンロードセンター"L4T Documentation"パッケージを検索してください。
docs.nvidia.com
ドキュメント内で、関連するトピックが次のように検索して見つかる場合があります。

Hardware Setup.

Configuring the 40-Pin Expansion Header.

Jetson-IO.

Platform Adaptation and Bring-Up.

Pinmux Changes.

## ダウンロードサイト
https://github.com/NVIDIA/jetson-gpio
