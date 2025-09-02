import streamlit as st
import google.generativeai as genai
from PIL import Image

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.set_page_config(page_title="Vision AI Assistant", layout="wide")

local_css("style.css")

genai.configure(api_key="AIzaSyC5aynhef2O3dzxD-howin-ylkD_agMb3k")

def get_gemini_response(input_text, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

st.sidebar.title("Vision AI Assistant")
st.sidebar.markdown("Upload an image and ask a question about it.")

input_prompt = st.sidebar.text_input("Input Prompt:", key="input")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
submit_button = st.sidebar.button("Analyze Image")

st.title("Image Analysis with Gemini")

if submit_button:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Your Image")
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Analysis Result")
            with st.spinner("Analyzing the image..."):
                response = get_gemini_response(input_prompt, image)
            st.write(response)
            st.markdown('</div>', unsafe_allow_html=True)
            
    else:
        st.warning("Please upload an image first.")
else:
    st.info("Upload an image and click 'Analyze Image' to get started.")

st.markdown('<div class="footer">Developed with ❤️ by Your Name</div>', unsafe_allow_html=True)
