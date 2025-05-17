# 🧠 FakeImageDetector


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
- OpenCV 
- NumPy  
- Pandas  
- Matplotlib / Seaborn  

## 📂 Dataset

The model is trained on the **CIFAKE** dataset from Kaggle:

- 60,000 real images (from CIFAR-10)  
- 60,000 AI-generated images (via Stable Diffusion v1.4)  
- Balanced dataset with equal real and fake samples  
- Dataset URL: [CIFAKE - Real and AI-Generated Synthetic Images](https://www.kaggle.com/datasets/skyhigh129/fake-vs-real-cifa10-cifake)  


## 🖼️ Image Classification  

**Image classification** is a computer vision task where an algorithm predicts a class label for a given input image. The model learns to extract relevant features from the image and processes them to produce an output—in this case, determining whether the image is **real or synthetic (AI-generated)**.  

### 🔍 How It Works  
- **Feature Extraction**: The model identifies patterns (edges, textures, shapes) from pixel data.  
- **Classification**: The extracted features are analyzed to assign a label (e.g., "real" or "synthetic").  
- **Output**: A confidence score or binary prediction is returned.  

### 🚀 Why It Matters  
- Detects AI-generated images (e.g., Deepfakes, GAN outputs).  
- Enhances authenticity verification in digital media.  
- Built using **Neural Networks** for high accuracy.
- 
## 🧮 Algorithm Used
### Neural Networks
- also known as Artificial Neural Networks (ANNs), are a class of algorithms inspired by the structure and functioning of the human brain. It consists of interconnected nodes organized into layers. These layers typically include an input layer, one or more hidden layers, and an output layer. Each connection between nodes has an associated weight, and nodes within a layer may have activation functions.
### Why Neural Networks?
- In image classification, neural networks excel at capturing subtle patterns and variations that conventional algorithms may find challenging. Their hierarchical structure allows them to proficiently learn and represent features across diverse levels of abstraction, proving highly effective for the specific requirements of image classification tasks.

## 📐 Model Architecture
### Convolutional Neural Network (CNN)
- a type of deep learning model architecture designed specifically for processing structured grid data, such as images. CNNs have proven to be highly effective in computer vision tasks, including image classification, object detection, segmentation, and more. They are characterized by their ability to automatically and adaptively learn spatial hierarchies of features directly from the data.

### Why CNN?
- CNNs have proven to be highly effective in computer vision tasks due to their ability to automatically and adaptively learn spatial hierarchies of features directly from diverse data sources such as images and videos.
## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.7+  
- `pip` package manager  

### 📦 Installation

Clone the repository:

```bash
git clone https://github.com/adam-ben-rhaiem/FakeImageDetector.git
cd FakeImageDetector
