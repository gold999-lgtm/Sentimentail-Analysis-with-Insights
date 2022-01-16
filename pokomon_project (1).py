

import os
print(os.getcwd())

from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense

classifier=Sequential()
classifier.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Conv2D(32,(3,3),activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Flatten())
classifier.add(Dense(units=128,activation="relu"))
classifier.add(Dense(units=3,activation="softmax"))
classifier.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])

from keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1./255,
                                 shear_range=0.2,
                                 zoom_range=0.2,
                                 horizontal_flip=True)
test_datagen=ImageDataGenerator(rescale=1.0/255)
training_set=train_datagen.flow_from_directory("C:/Users/Swati Lohiya/Downloads/dataset-20220115T072053Z-001/dataset/training_set",
                                               target_size=(64,64),
                                               batch_size=32,
                                               class_mode="categorical")
test_set=test_datagen.flow_from_directory("C:/Users/Swati Lohiya/Downloads/dataset-20220115T072053Z-001/dataset/test_set",
                                               target_size=(64,64),
                                               batch_size=32,
                                               class_mode="categorical")

print(type(training_set))
print(type(train_datagen))
classifier.fit_generator(training_set,
                         steps_per_epoch=100,
                         epochs=5,
                         validation_data=test_set,
                         validation_steps=200)
from keras.models import model_from_json
model_json=classifier.to_json()
with open("model_json","w") as json_file:
    json_file.write(model_json)
    
classifier.save_weights("model.h5")
import numpy as np
from keras.preprocessing import image
test_image=image.load_img("C:/Users/Swati Lohiya/Downloads/dataset-20220115T072053Z-001/dataset/single_prediction/pokemon1.png",target_size=(64,64))
test_image=image.img_to_array(test_image)

test_image=np.expand_dims(test_image,axis=0)
"""print(test_image.shape)
print(test_image.ndim)"""
predictions=classifier.predict(test_image)
"""print(np.argmax(classifier.predict(test_image), axis=-1))
print(predictions.ndim)
print(training_set.class_indices)
print((predictions>0.5).astype("int32"))"""
l=0
for i in training_set.class_indices:
  for k in (predictions>0.5).astype("int32"):
    while l<len(k):
      if k[l]==1:
        print(i)
        l+=1
        break
      l+=1
      break



