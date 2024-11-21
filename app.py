from PIL import Image
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model


IMG_HEIGHT = 32  # Set to the size expected by the model
IMG_WIDTH = 32

def predict_img(uploaded_file, model):
    # Step 1: Open the image and resize to (32, 32)
    img = Image.open(uploaded_file).resize((IMG_WIDTH, IMG_HEIGHT))

    # Step 2: Convert the image to a numpy array and normalize to [0, 1]
    img_array = np.array(img) / 255.0  # Normalize pixel values

    # Step 3: Add the batch dimension to match the input shape (None, 32, 32, 3)
    img_array = np.expand_dims(img_array, axis=0)

    # Step 4: Make the prediction
    prediction = model.predict(img_array)

    # Step 5: Interpret the result
    return "Real Image" if prediction[0] > 0.5 else "AI-Generated Image"
  


# Load the pre-trained model
model = load_model('real_vs_fake_image_classifier.h5')

def main():
    st.title("AI-Generated Image Detection")

    st.write("Upload an image to check if it's AI-generated or real.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Make prediction
        result = predict_img(uploaded_file, model)
        st.write(f"Prediction: **{result}**")

if __name__ == "__main__":
    main()


