# File: streamlit_image_to_text.py

import streamlit as st
import requests

# API ma'lumotlari
API_URL = 'https://api.api-ninjas.com/v1/imagetotext'
API_KEY = 'GV33D0f7Xxd0Dviil6nnvw==ITenHLuerFIbBuAK'

def convert_image_to_text(image_file):
    """Tasvirni matnga aylantiradi API orqali"""
    files = {'image': image_file}
    headers = {'X-Api-Key': API_KEY}
    response = requests.post(API_URL, files=files, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API xatosi: {response.status_code}, {response.text}")
        return None

# Streamlit UI
st.title("Tasvirni Matnga Aylantirish")
st.write("Tasvirni yuklang va uni matnga aylantiring!")

uploaded_file = st.file_uploader("Tasvir yuklash", type=["jpeg", "jpg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Yuklangan tasvir", use_container_width=True)
    
    if st.button("Tasvirni Matnga Aylantirish"):
        with st.spinner("Matn olinmoqda..."):
            result = convert_image_to_text(uploaded_file)
            if result:
                extracted_text = "\n".join([item['text'] for item in result])
                st.text_area("Aniqlangan Matn", extracted_text, height=200)
                
                # Faylni yuklab olish uchun tugma
                st.download_button(
                    label="Natijani Yuklab Olish",
                    data=extracted_text,
                    file_name="result.txt",
                    mime="text/plain"
                )
