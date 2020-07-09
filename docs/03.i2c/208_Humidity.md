# 208 Humidity

```
git clone https://github.com/FaBoPlatform/FaBoHumidity-HTS221-Python.git
cd FaBoHumidity-HTS221-Python
sudo pip3 install .
```


```
# coding: utf-8
import FaBoHumidity_HTS221
import time
import sys

hts221 = FaBoHumidity_HTS221.HTS221()

try:
    while True:
        h = hts221.readHumi()
        t = hts221.readTemp()
        sys.stdout.write("\rHumidity=%f,Temp=%f" % (h, t))
        sys.stdout.flush()
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
```

