# install dependencies
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load('yolov5', 'custom',
                       path='best.pt', source='local')
# 터미널 위치 따라서 경로가 달라지니까 조심
img = "tomato_green.jpg"

results = model(img)
# results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

print(len(results.xyxy[0]))
