from predict_and_box import predict_and_box
import cv2
import numpy as np
import os
import imghdr
from classify import predict_algae

def process_image(image_path):
    image_type = imghdr.what(image_path)
    if image_type not in ['png', 'jpeg']:
        return False
    elif image_type == 'jpeg':
        image = cv2.imread(image_path)
        png_path = os.path.splitext(image_path)[0] + '.png'
        cv2.imwrite(png_path, image)
        image_path = png_path

    image = cv2.imread(image_path)
    image = cv2.resize(image, (256, 256))
    prediction = predict_algae(image)

    # Draw bounding boxes on image
    for box in prediction:
        x1, y1, x2, y2 = box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return image, prediction, True