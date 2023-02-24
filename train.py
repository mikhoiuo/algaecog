# there is PROBABLY a better way to do this. but i am stupid.
# import shit yk the drill
import csv
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing import image
import numpy as np

# csv -> here
with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    X = []
    y = []
    for row in reader:
        # resize
        img = image.load_img(row[0], target_size=(256, 256))
        # normalification hypno
        x = image.img_to_array(img) / 255.0
        X.append(x)
        y.append(float(row[1]))

# numpification hypno
X = np.array(X)
y = np.array(y)

# sets
train_ratio = 0.6
val_ratio = 0.2
test_ratio = 0.2
train_size = int(train_ratio * len(X))
val_size = int(val_ratio * len(X))
test_size = len(X) - train_size - val_size

train_X = X[:train_size]
train_y = y[:train_size]
val_X = X[train_size:train_size+val_size]
val_y = y[train_size:train_size+val_size]
test_X = X[-test_size:]
test_y = y[-test_size:]

model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=(256, 256, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.fit(train_X, train_y, batch_size=32, epochs=10, validation_data=(val_X, val_y))

# eval of course i'm a classy dude
test_loss, test_acc = model.evaluate(test_X, test_y)
print('Test accuracy:', test_acc)
