# will eventually be changed bc i want to web implement. just for testing

import cv2
import numpy as np
from classify import predict_algae

def predict_and_box(model, image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (256, 256))

    boxes = predict_algae(model, image)

    # draw the bounding boxes on the image (want to make sure it WORKS)
    for box in boxes:
        x1, y1, x2, y2 = box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Show the image
    cv2.imshow("boxes babey!!!!!", image)
    cv2.waitKey(0)