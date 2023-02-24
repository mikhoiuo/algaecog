import os
import imghdr
import cv2
from predict_and_box import predict_and_box

def process_image(image_path):
    image_type = imghdr.what(image_path)
    if image_type not in {'png', 'jpeg'}:
        return None

    if image_type == 'jpeg':
        # convert
        png_path = os.path.splitext(image_path)[0] + '.png'
        image = cv2.imread(image_path)
        cv2.imwrite(png_path, image)
        image_path = png_path
    else:
        image = cv2.imread(image_path)

    # boxes...
    prediction = predict_and_box(model, image_path)

    return image, prediction, True
