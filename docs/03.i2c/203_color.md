# 203 Color

```
git clone https://github.com/FaBoPlatform/FaBoColor-S11059-Python.git
cd FaBoColor-S11059-Python
sudo pip3 install .
```


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

