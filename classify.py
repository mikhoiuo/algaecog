
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

model = load_model('algae_model.h5')

def predict_algae(img_path):
    # preprocess img 2 fit the model
    img = image.load_img(img_path, target_size=(256,256))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    # the MAGIC baby!!!
    prediction = model.predict(x)[0]
    return prediction