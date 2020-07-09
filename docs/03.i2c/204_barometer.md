# 204 Barometer

```
git clone https://github.com/FaBoPlatform/FaBoBarometer-MPL115-Python.git
cd FaBoBarometer-MPL115-Python
sudo pip3 install .
```


```
# coding: utf-8
import FaBoBarometer_MPL115
import time
import sys

mpl115 = FaBoBarometer_MPL115.MPL115()

try:
    while True:
        d  = mpl115.readData()
        h = mpl115.readHpa(212.0)

        sys.stdout.write("\rhda = %f, temp = %f, hda_aizu = %f" % (d['hpa'],  d['temp'], h))
        sys.stdout.flush()

        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
```

