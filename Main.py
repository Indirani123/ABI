!pip install ultralytics opencv-python-headless matplotlib
from google.colab import files
uploaded = files.upload()
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
# Get uploaded image path
image_path = list(uploaded.keys())[0]

# Run detection
results = model(image_path)

# Visualize result
results[0].show()
from IPython.display import Image, display
import os

# Save and show image
results[0].save(filename='result.jpg')
img = cv2.imread('result.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 8))
plt.imshow(img)
plt.axis('off')
plt.title("YOLOv8 Car Damage Detection")
plt.show()
