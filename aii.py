import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Constants for image size (adjust these to match your model input size)
IMG_HEIGHT = 224
IMG_WIDTH = 224

def main():
    st.title("AI-Generated Image Detection")

    st.write("Upload an image to check if it's AI-generated or real.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Make prediction
        prediction = predict_img(uploaded_file, model)
        st.write(f"Prediction: {prediction}")

if __name__ == "__main__":
    main()
