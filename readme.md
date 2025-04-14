# ECG Arrhythmia Detection using MIT-BIH Dataset

This project focuses on classifying ECG signals to detect various types of arrhythmia using machine learning and deep learning techniques. We utilize the MIT-BIH Arrhythmia Database from PhysioNet (via Kaggle) and adapt an existing implementation to train and evaluate our model.

## 📁 Repository Contents

- `p.ipynb` - Main notebook containing data preprocessing, model training, and evaluation steps.
- Cloned base repo from: [omroy07/Ecg_recognition](https://github.com/omroy07/Ecg_recognition)
- `plots/` - Visualizations of training performance and confusion matrix.
- `README.md` - Project overview and documentation.

## 📊 Dataset

**MIT-BIH Arrhythmia Database**  
📎 [MIT-BIH Dataset on Kaggle](https://www.kaggle.com/datasets/mondejar/mitbih-database)

- Contains 48 half-hour excerpts of two-channel ambulatory ECG recordings.
- Labeled with five types of heartbeat classes based on AAMI EC57 standard.
- Files: `mitbih_train.csv`, `mitbih_test.csv`

## 🧠 Technologies Used

- Python
- Jupyter Notebook
- NumPy, Pandas
- Matplotlib, Seaborn
- Scikit-learn
- TensorFlow / Keras
- Kaggle API

## 👨‍💻 Team Members & Roles

| Name              | Role                                | GitHub Username |
|-------------------|--------------------------------------|------------------|
| Teammate 1        | Team Lead / Project Manager          | @omroy07    |
| Teammate 2        | Data Collection & Preprocessing      | @username2       |
| Teammate 3        | Model Development (CNN/LSTM)         | @username3       |
| Teammate 4        | Evaluation / Hyperparameter Tuning   | @username4       |
| Teammate 5        | Research & Benchmark Comparison      | @username5       |
| Teammate 6        | Documentation & Final Presentation   | @username6       |

## 📝 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/omroy07/Ecg_recognition.git
   cd Ecg_recognition
