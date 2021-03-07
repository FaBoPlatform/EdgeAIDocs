import jetson.inference
import jetson.utils

net = jetson.inference.imageNet("googlenet")
font = jetson.utils.cudaFont()
camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")
display = jetson.utils.glDisplay()

while display.IsOpen():
        img, width, height = camera.CaptureRGBA()
        class_idx, confidence = net.Classify(img, width, height)
        class_desc = net.GetClassDesc(class_idx)     
        font.OverlayText(img, width, height, "{:05.2f}% {:s}".format(confidence * 100, class_desc), 5, 5, font.White, font.Gray40)
        display.RenderOnce(img, width, height)
        display.SetTitle("{:s} | Network {:.0f} FPS".format(net.GetNetworkName(), net.GetNetworkFPS()))
        net.PrintProfilerTimes()
