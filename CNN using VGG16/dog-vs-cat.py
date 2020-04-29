import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Input,Lambda,Dense,Flatten
from keras.models import models

from keras.applications.vgg16 import VGG16

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential

from glob import glob

from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image

train_path = 'train/train'
test_path = 'test1/test1'

batch_size = 32

val_datagen = ImageDataGenerator(rescale=1./255)



validation_generator = val_datagen.flow_from_directory(
        test_path,
        target_size=(224,224),
        batch_size=batch_size,
        class_mode='categorical')

        




















