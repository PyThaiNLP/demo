import streamlit as st
import time
from pythainlp.transliterate import transliterate

st.markdown("""
# Translation 🎉

PyThaiNLP support transliterate text for NLP piplines. We have

- thaig2p - (default) Thai Grapheme-to-Phoneme, output is IPA (require PyTorch)
- tltk_g2p - Thai Grapheme-to-Phoneme from TLTK <https://pypi.org/project/tltk/>_.,
- tltk_ipa - tltk, output is International Phonetic Alphabet (IPA)

for this demo page. You can custom dictionary for some word tokenizer engine. (Python only)
""")

with st.form("my_form"):
    st.write("Input word")
    text = st.text_input("text")
    engine=st.selectbox('Select transliterate', ['thaig2p', 'tltk_g2p', 'tltk_ipa'], key=1,index=0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.subheader("Words: ")
        start = time.time()
        st.write(transliterate(str(text), engine=str(engine)))
        end = time.time()
        st.write()
        st.write("Running times: "+str(end - start))

st.write("See the documentation at [transliterate | PyThaiNLP](https://pythainlp.github.io/docs/3.0/api/transliterate.html).")
