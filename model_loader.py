from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np
import os

# Загружаем модель (будет ждать model.h5 в папке model/)
MODEL_PATH = os.path.join("model", "model.h5")
model = load_model(MODEL_PATH)

def predict_image(img_path):
    """
    Возвращает 'cat' или 'dog' для переданного изображения
    """
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    pred = model.predict(img_array)
    return "dog" if pred[0][0] > 0.5 else "cat"
