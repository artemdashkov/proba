from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model():
    model = pipeline("sentiment-analysis",
                      "blanchefort/rubert-base-cased-sentiment")
    return model

def get_text():
    get_text = st.text_input(label='Введите текст: ')
    if get_text is not None:
        return get_text.lower()
    else:
        None

model = load_model()
st.title ('Распознавание текста')
text = get_text()

if text:
    result = model(text)[0]
    if result.get('label') == 'POSITIVE':
        st.write(f"Фраза позитивная с вероятностью {result.get('score'):.2%} \n")
    elif result.get('label') == 'NEUTRAL':
        st.write(f"Фраза нейтральная с вероятностью {result.get('score'):.2%} \n")
    else:
        st.write(f"Фраза негативная с вероятностью {result.get('score'):.2%} \n")

# while text != "выход":
#     result = model(text)[0]
#     if result.get('label') == 'POSITIVE':
#         st.write(f"Фраза позитивная с вероятностью {result.get('score'):.2%} \n")
#     elif result.get('label') == 'NEUTRAL':
#         st.write(f"Фраза нейтральная с вероятностью {result.get('score'):.2%} \n")
#     else:
#         st.write(f"Фраза негативная с вероятностью {result.get('score'):.2%} \n")
#
#     text = input ("Текст: ").lower()