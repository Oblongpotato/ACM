import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import os
from django.conf import settings

# Load the pre-trained model
model_path = os.path.join(settings.BASE_DIR, 'Model', 'model.h5')
model = tf.keras.models.load_model(model_path, custom_objects={'BatchNormalization': tf.keras.layers.BatchNormalization})

# Define the labels
emotion_labels = ['confident', 'not confident']


def predict_confidence(image_file):
    
    # Open the uploaded file as an image
    image = Image.open(image_file).convert('RGB')
    
    # Convert the uploaded image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    # Resize the image to match the input size expected by the model
    gray_image = cv2.resize(gray_image, (48, 48), interpolation=cv2.INTER_AREA)

    # Preprocess the image for model prediction
    roi = gray_image.astype('float') / 255.0  # Normalize the pixel values
    roi = tf.keras.utils.img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)  # Add batch dimension

    # Make a prediction
    prediction = model.predict(roi)[0]
    label = emotion_labels[prediction.argmax()]

    return label
