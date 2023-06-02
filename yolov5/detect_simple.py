#install dependencies
import torch 
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load('runs/train/fruit_yolov5s_results5', 'yolov5s')
