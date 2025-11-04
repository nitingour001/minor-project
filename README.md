# Phishing URL Detection Tool (Minor Project)

A simple machine-learning based phishing URL detector. Enter a URL and the app
extracts a set of handcrafted features and predicts whether it is **Phishing** or **Legitimate**.

## Features used
- URL length, domain length, number of dots/sub-directories
- Presence of IP address in URL
- Use of `https`
- Suspicious TLD (e.g., `.zip`, `.xyz`, `.top`, `.gq`, `.tk`, ...)
- Use of `@`, `-` in domain
- Length of query string
- Ratio of digits
- Keyword triggers (e.g., `login`, `verify`, `update`, `secure`, `account`, `bank`, `confirm`, `signin`)
- Shortener domains (e.g., bit.ly, tinyurl.com, t.co)
- Shannon entropy of the URL string

> This is a **teaching/demo** project — not production security software.

## Project Structure
```
phishing-url-detector/
├── app.py               # Streamlit app
├── features.py          # Feature extraction
├── train.py             # Trains Logistic Regression from sample_data.csv
├── sample_data.csv      # Tiny demo dataset (URL,label)
├── model.pkl            # Saved trained model (created by train.py)
├── requirements.txt
├── README.md
└── LICENSE
```

## Quick Start

1. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Retrain the model:**
   ```bash
   python train.py
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

5. **CLI quick test (without Streamlit):**
   ```bash
   python -c "from features import extract_features; import pickle, json; import sys; m=pickle.load(open('model.pkl','rb')); u='http://update-login-secure.tinyurl.com/bank/verify?acc=12345'; print('URL:',u); print('pred:',('Phishing','Legitimate')[int(m.predict([extract_features(u)])[0])]); print('proba:',m.predict_proba([extract_features(u)])[0].tolist())"
   ```

## Dataset Notes
`sample_data.csv` is a synthetic, small dataset suitable for class demos. For better performance,
replace it with a larger, real dataset and retrain using `train.py`.

## Academic Notes
Include this repo as a minor project: covers basic ML pipeline, feature engineering, model persistence,
and a simple UI (Streamlit). You can expand with more features, models, or datasets.
