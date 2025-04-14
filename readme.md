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
- Files: `100.csv`, `100annotations.txt`and so on.

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
| Teammate 1        | Team Lead / Project Manager          | Om Roy    |
| Teammate 2        | Data Collection & Preprocessing      | Kanisha Ravindra Sharma|
| Teammate 3        | Model Development (CNN/LSTM)         | Anshuman Pandey     |
| Teammate 4        | Evaluation / Hyperparameter Tuning   | Tanmay Pandey       |
| Teammate 5        | Research & Benchmark Comparison      | Samridhi Saxena      |
| Teammate 6        | Documentation & Final Presentation   | Elfa Monali |

## 📝 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/omroy07/Ecg_recognition.git
   cd Ecg_recognition
``
## 📥 Download the Dataset

1. Go to the [Kaggle Dataset](https://www.kaggle.com/datasets/mondejar/mitbih-database)
2. Download and extract the files:  
   - `mitbih_train.csv`  
   - `mitbih_test.csv`  
3. Place them in the same directory as your notebook.

## 🚀 Launch the Jupyter Notebook

```bash
jupyter notebook p.ipynb
```
## 🚀 Future Enhancements

- Improve accuracy using deeper or hybrid models (e.g., CNN + LSTM)
- Explore Transformer-based architectures
- Add real-time ECG signal processing support
- Deploy the model using Flask or Streamlit
- Implement explainability tools like Grad-CAM or SHAP
