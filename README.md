# 🧠 Fake vs Real Image Classification using CNN

![Project Banner](https://your-image-link.com/banner.jpg) <!-- Optional: Replace with a relevant banner image URL -->

## 📌 Overview

This project implements a **Convolutional Neural Network (CNN)** to classify images as either **real or AI-generated**.  
With the rapid advancement of AI image generation technologies, distinguishing between real and synthetic images has become increasingly important for:

- ✅ Content verification  
- 🕵️‍♀️ Digital forensics  
- 📸 Media authenticity  

## ✨ Features

- 🧠 CNN-based classification of images as real or AI-generated  
- 💻 Streamlit web interface for easy user interaction  
- 🧾 Trained on the [CIFAKE dataset](https://www.kaggle.com/datasets/skyhigh129/fake-vs-real-cifa10-cifake) from Kaggle  
- 🔼 Simple, intuitive UI for image upload and prediction  
- 📊 Displays prediction confidence scores  

## 🛠️ Technologies Used

- Python 3.x  
- TensorFlow / Keras  
- Streamlit  
- OpenCV / Pillow  
- NumPy  
- Pandas  
- Matplotlib / Seaborn  

## 📂 Dataset

The model is trained on the **CIFAKE** dataset from Kaggle:

- 60,000 real images (from CIFAR-10)  
- 60,000 AI-generated images (via Stable Diffusion v1.4)  
- Balanced dataset with equal real and fake samples  
- Dataset URL: [CIFAKE - Real and AI-Generated Synthetic Images](https://www.kaggle.com/datasets/skyhigh129/fake-vs-real-cifa10-cifake)  

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.7+  
- `pip` package manager  

### 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fake-real-image-classification.git
cd fake-real-image-classification
