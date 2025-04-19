# 🌾 Crop Recommendation System

## 📖 About the Dataset

This dataset is designed for building a **Crop Recommendation System** using machine learning. Precision agriculture is becoming increasingly important as it empowers farmers to make informed decisions on crop selection based on environmental and soil conditions. This dataset helps facilitate that by offering a combination of soil, climate, and rainfall features.

## 🧠 Context

The dataset was created by combining and augmenting publicly available datasets on rainfall, climate, and fertilizer data specific to **India**. The goal is to enable the development of intelligent systems that recommend the most suitable crop for a particular region or soil condition.

## 📊 Dataset Features

Each row in the dataset represents a record of environmental parameters and the corresponding recommended crop. Below are the features:

| Feature       | Description                                      |
|---------------|--------------------------------------------------|
| `N`           | Ratio of Nitrogen content in the soil            |
| `P`           | Ratio of Phosphorous content in the soil         |
| `K`           | Ratio of Potassium content in the soil           |
| `temperature` | Temperature in °C                                |
| `humidity`    | Relative humidity in %                           |
| `ph`          | pH value of the soil                             |
| `rainfall`    | Rainfall in mm                                   |
| `label`       | Target crop label (e.g., rice, maize, wheat, etc.) |

## 📥 Download the Dataset

📁 [Download the dataset from Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

To use the dataset in your project:
1. Download the CSV file from the Kaggle link above.
2. Place it in your project directory (e.g., `data/crop_recommendation.csv`).

## 🔍 Example Use Cases

- Crop recommendation systems
- Soil quality analysis
- Climate-aware farming tools
- Machine learning pipelines for agriculture

## 🚀 Getting Started

You can load the dataset using `pandas`:

```python
import pandas as pd

df = pd.read_csv('crop_recommendation.csv')
print(df.head())
