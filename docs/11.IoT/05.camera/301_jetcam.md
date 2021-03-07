# 301 JetCam

```
git clone https://github.com/NVIDIA-AI-IOT/jetcam
cd jetcam
sudo python3 setup.py install
```


```
from jetcam.csi_camera import CSICamera
import ipywidgets
from IPython.display import display
from jetcam.utils import bgr8_to_jpeg

camera = CSICamera(width=224, height=224)
image = camera.read()

image_widget = ipywidgets.Image(format='jpeg')
image_widget.value = bgr8_to_jpeg(image)
display(image_widget)
```

カメラ画像の更新
```
camera.running = True

def update_image(change):
    image = change['new']
    image_widget.value = bgr8_to_jpeg(image)
    
camera.observe(update_image, names='value')
```

## Cameraの再起動

```
sudo systemctl restart nvargus-daemon
```

## Cameraの状態を確認

```
journalctl -u nvargus-daemon.service -f
```



