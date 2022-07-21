import streamlit as st
import time
from pythainlp.tokenize import word_tokenize
st.markdown("""
# Word tokenization 🎉

PyThaiNLP support Word tokenization for NLP piplines. We have

- newmm (default) - dictionary-based, Maximum Matching + Thai Character Cluster
- mm - dictionary-based, Maximum Matching
- longest - dictionary-based, Longest Matching
- tltk - wrapper for TLTK.

for this demo page. You can custom dictionary for some word tokenizer engine. (Python only)
""")
with st.form("my_form"):
    st.write("Input text")
    text = st.text_area("text")
    engine=st.selectbox('Select word tokenizition', ['newmm', 'mm', 'longest', 'tltk'], key=1,index=0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.subheader("Words: ")
        start = time.time()
        st.write(' '.join(word_tokenize(str(text), engine=str(engine))))
        end = time.time()
        st.write()
        st.write("Running times: "+str(end - start))

st.write("See the documentation at [word_tokenize | PyThaiNLP](https://pythainlp.github.io/docs/3.0/api/tokenize.html#pythainlp.tokenize.word_tokenize).")
#st.sidebar.markdown("# Word tokenize 🎉")

