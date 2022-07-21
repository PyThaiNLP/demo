import streamlit as st
import time
from pythainlp.tokenize import sent_tokenize
st.markdown("""
# Sentence tokenization 🎉

PyThaiNLP support Sentence tokenization for NLP piplines. We have

- crfcut - (default) split by CRF trained on TED dataset.
- whitespace+newline - split by whitespaces and newline.
- whitespace - split by whitespaces. Specifiaclly, with regex pattern r" +"
- tltk - split by TLTK.

for this demo page.
""")

with st.form("my_form"):
    st.write("Input text")
    text = st.text_area("text")
    engine=st.selectbox('Select sentence tokenizer', ['crfcut', 'whitespace+newline', 'whitespace', 'tltk'], key=1,index=0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.subheader("Sentences: ")
        start = time.time()
        _temp = sent_tokenize(str(text), engine=str(engine))
        for i in _temp:
            st.write(i)
        end = time.time()
        st.write()
        st.write("Running times: "+str(end - start))

st.write("See the documentation at [sent_tokenize | PyThaiNLP](https://pythainlp.github.io/docs/3.0/api/tokenize.html#pythainlp.tokenize.sent_tokenize).")
#st.sidebar.markdown("# Word tokenize 🎉")
