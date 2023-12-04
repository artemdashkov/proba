# from transformers import pipeline
import io
from keras.applications import EfficientNetB0
from keras.applications.efficientnet import preprocess_input
from keras.applications.efficientnet import decode_predictions
from keras.preprocessing import image
import numpy as np

import streamlit as st
from PIL import Image

@st.cache(allow_output_mutation=True)
def load_model():
    model = EfficientNetB0(weights='imagenet')
    return model

def load_image ():
    uploaded_file = st.file_uploader("Вставьте изображение")
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None

def preprocess_image(img):
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_image(x)
    return x

def print_prediction(preds):
    classes = decode_predictions(preds, top=3)[0]
    for cl in classes:
        st.write(cl[1], cl[2])

model = load_model()
st.title ('Распознавание изображений')
img = load_image()
result = st.button("Распознать изображение")

if result:
    x = preprocess_image(img)
    preds = model.predict(x)
    st.write("**Результаты распознавания:**")
    print_prediction(preds)

# classifier = pipeline("sentiment-analysis",
#                       "blanchefort/rubert-base-cased-sentiment")
#
# print("Привет! Ниже вам необходимо ввести текст для определения его эмоциональной окраски. Для выхода из приложения"
#       "достаточно в поле 'Текст' ввести слово 'выход'.")
# text = input ("Текст: ").lower()
#
# while text != "выход":
#     result = classifier(text)[0]
#     if result.get('label') == 'POSITIVE':
#         print(f"Фраза позитивная с вероятностью {result.get('score'):.2%} \n")
#     elif result.get('label') == 'NEUTRAL':
#         print(f"Фраза нейтральная с вероятностью {result.get('score'):.2%} \n")
#     else:
#         print(f"Фраза негативная с вероятностью {result.get('score'):.2%} \n")
#
#     text = input ("Текст: ").lower()
# print("Выполнен выход из приложения.")