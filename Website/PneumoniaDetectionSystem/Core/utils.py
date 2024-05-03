from keras.models import load_model
import cv2
import numpy as np

def load_trained_model(model_path):
    loaded_model = load_model(model_path)
    loaded_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return loaded_model

def preprocess_image(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img / 255.0
    img = np.reshape(img, (1, 224, 224, 1))  # Add batch dimension
    return img

def predict_image_class(model, img_path):
    image = preprocess_image(img_path)
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions)
    return predicted_class, predictions
