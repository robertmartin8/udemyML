"""
Created on Mon Apr 24 11:24:23 2017

@author: Robert
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialise the CNN
clf = Sequential()

# Convolution
clf.add(Convolution2D(32, (3, 3), input_shape = (64, 64,3), activation = 'relu'))

# Max pooling
clf.add(MaxPooling2D(pool_size = (2,2)))

# Second convolution
clf.add(Convolution2D(32, (3,3), activation = 'relu'))

# Flattening
clf.add(Flatten())

# Full connection
clf.add(Dense(units = 128, activation = 'relu'))
clf.add(Dense(units = 128, activation = 'relu'))
clf.add(Dense(units = 1, activation = 'sigmoid'))

clf.compile(optimizer = "adam", loss = "binary_crossentropy", 
            metrics = ['accuracy'])

# Image preprocessing
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train = train_datagen.flow_from_directory('dataset/training_set',
                                          target_size=(64, 64),
                                          batch_size=32,
                                          class_mode='binary')

test = test_datagen.flow_from_directory('dataset/test_set',
                                        target_size=(64, 64),
                                        batch_size=32,
                                        class_mode='binary')

clf.fit_generator(train,
                  nb_epoch = 15, 
                  validation_data = test,
                  nb_val_samples = 2000)

