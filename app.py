import streamlit as st
import pickle
from features import extract_features

st.set_page_config(page_title='Phishing URL Detector', page_icon='🔒')

st.title('🔒 Phishing URL Detection Tool')
st.write('Enter a URL to predict whether it is **Phishing** or **Legitimate**.')

@st.cache_resource
def load_model():
    with open('model.pkl','rb') as f:
        return pickle.load(f)

model = load_model()

url = st.text_input('URL', 'http://update-login-secure.tinyurl.com/bank/verify?acc=12345')

if st.button('Analyze'):
    feats = extract_features(url)
    proba = model.predict_proba([feats])[0]
    pred = int(model.predict([feats])[0])
    label = 'Legitimate ✅' if pred == 1 else 'Phishing ⚠️'
    st.subheader(f'Result: {label}')
    st.caption(f'Confidence (Legitimate vs Phishing): {proba[1]:.2%} vs {proba[0]:.2%}')

    names = [
        'url_len','num_dots','num_subdirs','query_len','uses_https','has_at',
        'ratio_digits','entropy','domain_len','has_ip','suspicious_tld','hyphen_in_domain',
        'is_shortener','keyword_hit'
    ]
    st.markdown('**Feature Breakdown**')
    st.json({k: v for k, v in zip(names, feats)})

st.info('Educational demo only. For real-world use, train on a larger, diverse dataset and add advanced features.')
