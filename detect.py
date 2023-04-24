# install dependencies
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load('', 'custom', path='best.pt', source='local')

img = "tomato885.png"

results = model(img)
results.pandas().xyxy[0]
