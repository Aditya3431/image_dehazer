import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="🌀 Image Dehazing Tool", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .upload-box {
        background: #ffffff;
        border-radius: 10px;
        padding: 2rem 2rem 1rem 2rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        display: inline-block;
        margin-top: 2rem;
    }
    .stButton>button {
        padding: 0.7rem 1.5rem;
        background: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
        cursor: pointer;
        transition: background 0.2s;
    }
    .stButton>button:hover {
        background: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:#2c3e50;text-align:center;'>🌀 Image Dehazing Tool</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Upload your hazy image, and we will clear it for you!</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a hazy image", type=["jpg", "jpeg", "png"], key="uploader")
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Hazy Image", use_column_width=True)

        # Placeholder for dehazing logic
        st.markdown("### Dehazed Image")
        # For demonstration, just show the original image as "dehazed"
        # Replace this with your dehazing model or algorithm
        st.image(image, caption="Dehazed Image (Demo)", use_column_width=True)
        st.success("Image dehazing complete! (Demo)")

st.markdown("""
---
<p style='text-align:center; color: #888;'>Made with ❤️ using Streamlit</p>
""", unsafe_allow_html=True)
