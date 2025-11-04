Phishing URL Detection Tool (Minor Project)

A simple machine-learning based phishing URL detector. Enter a URL and the app
extracts a set of handcrafted features and predicts whether it is Phishing or Legitimate.

Features used
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

> This is a teaching/demo project — not production security software.

Project Structure

phishing-url-detector/
├── app.py               # Streamlit app
├── features.py          # Feature extraction
├── train.py             # Trains Logistic Regression from sample_data.csv
├── sample_data.csv      # Tiny demo dataset (URL,label)
├── model.pkl            # Saved trained model (created by train.py)
├── requirements.txt
├── README.md
└── LICENSE

