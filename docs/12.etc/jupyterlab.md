## Jupyterlabの使い方

sshでログインしてpythonを実行できますが、Jupyter NoteBookおよびJupyter labは、豊富なリソースを利用し、WebブラウザからPythonを実行できます。また、画像やグラフなどを簡単に表示できデータ分析などに役立ち大変便利です。また、拡張機能のプラグインを取り込むことで機能を増やしたり、簡単に文章表現できるMarkDown記法にも対応しております。jupyter labは、jupyter notebookを進化させています。

## インストール

```sh
$sudo apt install nodejs npm
$sudo apt install python3-pip
$sudo pip3 install jupyter jupyterlab
```

## エラーが出た場合
```sh
$sudo apt-get install python3-dev
$sudo apt-get install libffi-dev
```

## jupyter labを起動
```sh
$chromium-browser --no-sandbox & jupyter lab
```
ipアドレスをしらべる。Wifiで接続する場合は、wan0の項目のIPアドレス
```sh
$ifconfig -a
```


## Jetson Nanoにアクセス
パソコンのブラウザ（Chrome,Firefox）アドレスバーに上記でしらべてIPアドレスを192.168.0.****と入力します。

※お使いの環境によります。

![](./img/jupyterlab/jupyterlabgamen01.jpg)

### python3のコードを記述する。

python3を選ぶ。

![](./img/jupyterlab/jypyterlabgamen02.png)

すると1つのセルが現れます。

![](./img/jupyterlab/jupyterlabgamen03.png)

renameを選択肢ファイルに名前をつけます。サンプルとしてhelloworld.ipynbと名前をつけます。

![](./img/jupyterlab/jupyterlabgamenrename.png)

セルに以下の１行コードを入力します。
```python
print("Hello World.")
```

![](./img/jupyterlab/jupyterlabgamen04.png)

入力し終わったら、上の横三角マークするとクリックすると
Hello World.
と表示することができたと思います。

ループなど停止する場合は、四角ボタンをクリックします。

## グラフを表示させる

左上にある+ボタンを押して、Lancherのタブにて、terminalを選択します。

つぎのパッケージをインストールします。


```sh
$sudo pip3 install cython
```

```sh
$sudo pip3 install -U pip testresources setuptools
```

```sh
$sudo pip3 install matplotlib
```

y　＝　２x　＋　１　の一次関数を描画する

```python

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 300, 1)
y = x * 2 + 1

plt.plot(x, y)
plt.show()

```

![](./img/jupyterlab/GraphDemo.png)


## Markdownの記述方法
タブ内の＋ボタンを押して、セルを追加します。Code->Markdownに変更します。
そのセルの中に ## グラフの描画　１次関数と入力します。

![](./img/jupyterlab/MarkDown01.png)

Shiftキー + enterキーを押すとマークダウンのテキストとして入力されコメントアウトよりも表現豊かに表記ができます。

![](./img/jupyterlab/MarkDown02.png)

## 数式をマークダウンで表記

関数など綺麗な文字を表現すること可能です。

セルを追加して、Markdownを選択して入力

![](./img/jupyterlab/suusiki01.png)

```
$$ y = 2x + 1 $$
```

![](./img/jupyterlab/suusiki02.png)


三角関数の例

```python

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 3.14, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()

```

```
$$ y = \sin\theta $$
```

![](./img/jupyterlab/suusiki03.png)


Markdown記法のくわしい情報は、help->Markdown Referenceに記載されています。

![](./img/jupyterlab/MarkDown03.png)

## 行番号の表記

viewからshow Line Numbersを選択

![](./img/jupyterlab/ShowLineNumber.png)

## ファイルのアップロード
SCPコマンドなどをつかうことなくファイルをアップロードします。

〜工事中写真〜

## ファイルのダウンロード

〜工事中写真〜


## プラグイン

〜工事中〜