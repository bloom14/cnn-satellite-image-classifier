# 🌍 Satellite Image Classification using CNN

## 📌 Overview
This project is an end-to-end Deep Learning application that classifies satellite images into different land-use categories using a Convolutional Neural Network (CNN).  

It also includes a Flask-based web application where users can upload an image and get real-time predictions.

---

## 🚀 Features
-  CNN model built using PyTorch  
-  Trained on EuroSAT RGB dataset  
- 📈 Achieved high classification accuracy (~90–95%)  
- 🌐 Web app using Flask for real-time predictions  
- 📊 Data preprocessing & augmentation  

---

## 📊 Dataset

This project uses the EuroSAT RGB dataset.

- Contains ~27,000 satellite images  
- 10 land-use classes:
  - AnnualCrop
  - Forest
  - HerbaceousVegetation
  - Highway
  - Industrial
  - Pasture
  - PermanentCrop
  - Residential
  - River
  - SeaLake  

Each image represents a specific type of land cover.

🔗 Dataset Link: https://github.com/phelber/eurosat  

---

## ⚙️ Preprocessing
- Images resized to 64×64  
- Random horizontal flip  
- Random rotation  
- Normalization applied  

---

## 🧠 Model Architecture
- Convolutional layers with ReLU activation  
- Batch Normalization for stability  
- MaxPooling for feature extraction  
- Dropout for overfitting prevention  
- Fully connected layers for classification  

---

## 🖥️ Web Application
The Flask app allows users to:
- Upload a satellite image  
- Get predicted land-use class instantly  

---

## 📂 Project Structure
