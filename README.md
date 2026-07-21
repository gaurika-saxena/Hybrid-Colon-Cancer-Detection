# Hybrid Colon Cancer Detection using CNN + GLCM + SVM

## Project Status

**Status:** Work in Progress

This repository contains my final-year Bachelor of Engineering project focused on developing a hybrid machine learning model for colon cancer detection from histopathological images.

The project combines deep learning and traditional machine learning techniques to improve classification performance while following software engineering best practices such as modular development, version control, and reproducible experimentation.

---

## Project Overview

The proposed hybrid pipeline combines convolutional neural networks with texture analysis and machine learning classification.

### Proposed Pipeline

```
Histopathological Images
        │
        ▼
Image Preprocessing
        │
        ▼
CNN Feature Extraction (ResNet50)
        │
        ▼
GLCM Texture Feature Extraction
        │
        ▼
Feature Fusion
        │
        ▼
SVM Classification
        │
        ▼
Performance Evaluation
```

---

## Dataset

**Dataset:** LC25000 Histopathological Image Dataset

**Classes Used**

- Colon Adenocarcinoma
- Colon Benign Tissue

---

## Technologies

- Python
- TensorFlow / Keras
- OpenCV
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- Git
- GitHub

---

## Repository Structure

```
Hybrid-Colon-Cancer-Detection/
│
├── data/
├── docs/
├── models/
├── outputs/
├── scripts/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Current Progress

- Completed: Project setup
- Completed: Git and GitHub repository initialization
- Completed: Dataset exploration
- Completed: Dataset preprocessing
- Completed: Train/Validation/Test dataset split
- In Progress: ResNet50 model training
- Planned: GLCM feature extraction
- Planned: Feature fusion
- Planned: SVM classifier development
- Planned: Model evaluation and performance comparison

---

## Future Enhancements

- Hyperparameter optimization
- Explainable AI using Grad-CAM
- Streamlit-based web application
- Performance comparison with additional machine learning models

---

## Author

**Gaurika Saxena**

Bachelor of Engineering (Information Science & Engineering)

Interested in Artificial Intelligence, Machine Learning, Computer Vision, and Data Analytics.