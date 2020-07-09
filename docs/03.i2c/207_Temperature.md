# 207 Temperature

```
git clone https://github.com/FaBoPlatform/FaBoTemperature-ADT7410-Python.git
cd FaBoTemperature-ADT7410-Python
sudo pip3 install .
```


```
# coding: utf-8

import FaBoTemperature_ADT7410
import time
import sys

adt7410 = FaBoTemperature_ADT7410.ADT7410()

try:
    while True:
        t = adt7410.read()
        sys.stdout.write("\rTemp=%f" % t)
        sys.stdout.flush()

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
```

