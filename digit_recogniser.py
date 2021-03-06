# -*- coding: utf-8 -*-
"""Digit_recogniser.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/109LpWoBb2R4_WWVJKpV_HUrPQ-i_w4GT
"""

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy as np

(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = mnist.load_data()

train_images= mnist_train_images.reshape(60000, 784)
test_images= mnist_test_images.reshape(10000, 784)

train_images= train_images.astype('float32')
test_images= test_images.astype('float32')

train_images= train_images/255
test_images= test_images/255 

print('train_images shape:' ,train_images.shape)
print(train_images.shape[0], 'train samples')
print(test_images.shape[0], 'test samples')

train_labels= keras.utils.to_categorical(mnist_train_labels, 10)
test_labels= keras.utils.to_categorical(mnist_test_labels, 10)

import matplotlib.pyplot as plt

def display_sample(num):
  print(train_labels[num])

  label= train_labels[num].argmax(axis=0)
  image= train_images[num].reshape([28, 28])
  plt.title('Sample: %d  Label %d' % (num, label))
  plt.imshow(image, cmap=plt.get_cmap('gray_r'))
  plt.show()

display_sample(2235)

model= Sequential()
model.add(Dense(512, activation='relu' , input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', 
              optimizer=RMSprop(),
              metrics=['accuracy'])

model.fit(train_images, train_labels,
                   batch_size=80,
                   epochs=10,
                   verbose=2,
                   validation_data=(test_images, test_labels))

score= model.evaluate(test_images, test_labels , verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# model_json= model.to_json()
# with open("model.json", "w") as json_file:
#   json_file.write(model_json)

model.save_weights("model.h5")
print("Saved model to disk")



# for x in range(1000):
#   test_image= test_images[x,:].reshape(1,784)
#   predicted_cat= model.predict(test_image).argmax()
#   label= test_labels[x].argmax()
#   if(predicted_cat!=label):
#     plt.title('prediction: %d Label: %d' %(predicted_cat, label))
#     plt.imshow(test_image.reshape([28,28]), cmap=plt.get_cmap('gray_r'))
#     plt.show()

# predict on the first 5 test images

predictions= model.predict(test_images[6:8])
# print(predictions)
print(np.argmax(predictions, axis=1))
print(test_labels[6:8])

for i in range(6,8):
  first_image= test_images[i]
  first_image= np.array(first_image, dtype='float')
  pixels= first_image.reshape((28,28))
  plt.imshow(pixels, cmap='gray_r')
  plt.show()

