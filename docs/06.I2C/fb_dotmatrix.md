# FB Dotmatrix

## Driverのインストール


```
pip3 install adafruit-circuitpython-ht16k33
```

## サンプルコード使用時の接続

```
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Basic example of clearing and drawing a pixel on a LED matrix display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

# Import all board pins.
import time
import board
import busio

# Import the HT16K33 LED matrix module.
from adafruit_ht16k33 import matrix


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

matrix = matrix.Matrix8x8(i2c, address=0x70)
matrix.fill(0)

for row in range(2, 6):
    matrix[row, 0] = 1
    matrix[row, 7] = 1

for column in range(2, 6):
    matrix[0, column] = 1
    matrix[7, column] = 1

matrix[1, 1] = 1
matrix[1, 6] = 1
matrix[6, 1] = 1
matrix[6, 6] = 1
matrix[2, 5] = 1
matrix[5, 5] = 1
matrix[2, 3] = 1
matrix[5, 3] = 1
matrix[3, 2] = 1
matrix[4, 2] = 1

# Move the Smiley Face Around
while True:
    for frame in range(0, 8):
        matrix.shift_right(True)
        time.sleep(0.05)
    for frame in range(0, 8):
        matrix.shift_down(True)
        time.sleep(0.05)
    for frame in range(0, 8):
        matrix.shift_left(True)
        time.sleep(0.05)
    for frame in range(0, 8):
        matrix.shift_up(True)
        time.sleep(0.05)
```