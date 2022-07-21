import streamlit as st
import time
from pythainlp.translate import Translate

st.markdown("""
# Translation 🎉

PyThaiNLP support machine translation for translate text. We have

- th2en - (default) Thai to English translation
- en2th - English to Thai translation
- th2zh - Thai to Chinese translation
- zh2th - Chinese to Thai translation
- th2fr - Thai to French translation

for this demo page. It will use many times for running model.
""")
_engine =None
with st.form("my_form"):
    st.write("Input text")
    text = st.text_area("text")
    engine=st.selectbox('Select', ['th2en', 'en2th', 'zh2th', 'th2zh', 'th2fr'], key=1,index=0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.subheader("Text: ")
        start = time.time()
        if engine=="th2en":
            from pythainlp.translate.en_th import download_model_all
            download_model_all()
            _engine = Translate('th', 'en')
        elif engine=="en2th":
            from pythainlp.translate.en_th import download_model_all
            download_model_all()
            _engine = Translate('en','th')
        elif engine == "zh2th":
            _engine = Translate("zh","th")
        elif engine == "th2zh":
            _engine = Translate("th","zh")
        elif engine == "th2fr":
            _engine = Translate("th", "fr")
        st.write(_engine.translate(str(text)))
        end = time.time()
        st.write()
        st.write("Running times: "+str(end - start))

st.write("See the documentation at [translate | PyThaiNLP](https://pythainlp.github.io/docs/3.0/api/translate.html).")
