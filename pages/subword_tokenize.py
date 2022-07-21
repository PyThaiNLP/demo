import streamlit as st
import time
from pythainlp.tokenize import subword_tokenize
st.markdown("""
# Subword tokenization 🎉

PyThaiNLP support Subword tokenization for NLP piplines. We have

- tcc (default) - Thai Character Cluster (Theeramunkong et al. 2000)
- etcc - Enhanced Thai Character Cluster (Inrut et al. 2001)
- dict - newmm word tokenizer with a syllable dictionary
- ssg - CRF syllable segmenter for Thai
- tltk - syllable tokenizer from tltk

for this demo page.
""")
with st.form("my_form"):
    st.write("Input text")
    _text = st.text_area("text")
    engine=st.selectbox('Select word tokenizition', ['tcc', 'etcc', 'dict', 'ssg', 'tltk'], key=1,index=0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.subheader("Subwords: ")
        start = time.time()
        st.write(' '.join(subword_tokenize(str(_text), engine=str(engine))))
        end = time.time()
        st.write()
        st.write("Running times: "+str(end - start))

st.write("See the documentation at [subword_tokenize | PyThaiNLP](https://pythainlp.github.io/docs/3.0/api/tokenize.html#pythainlp.tokenize.subword_tokenize).")
