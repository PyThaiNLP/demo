import streamlit as st
import time
from pythainlp.tag import pos_tag
from pythainlp.tokenize import word_tokenize
st.markdown("""
# Part of speech tagging 🎉

PyThaiNLP support part-of-speech tagging for analysis text. We have
- perceptron - perceptron tagger (default)
- unigram - unigram tagger
- tltk - TLTK: Thai Language Toolkit (support TNC corpus only. if you choose other corpus, It’s change to TNC corpus.)
and trained with corpus:
- lst20 - LST20 corpus by National Electronics and Computer Technology Center, Thailand
- orchid - ORCHID corpus, text from Thai academic articles
- pud - Parallel Universal Dependencies (PUD) treebanks, natively use Universal POS tags
- lst20_ud - LST20 text, with tags mapped to Universal POS tag from Universal Dependencies
- orchid_ud - ORCHID text, with tags mapped to Universal POS tags

for this demo page.
""")

with st.form("my_form"):
    st.write("Input text")
    text = st.text_area("text")
    word_engine=st.selectbox('Select word tokenize', ['newmm', 'mm', 'longest', 'tltk'], key=1,index=0)
    pos_corpus = st.selectbox('Select POS corpus', ['lst20', 'orchid', 'pud', 'lst20_ud', 'orchid_ud'], key=1,index=0)
    pos_engine = st.selectbox('Select Postag engine', ['perceptron', 'unigram', 'tltk'], key=1,index=0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.subheader("Pos: ")
        start = time.time()
        _list_words = word_tokenize(str(text), engine=str(word_engine))
        _pos = pos_tag(_list_words, corpus=str(pos_corpus), engine=str(pos_engine))
        _text = ""
        for i,j in _pos:
            _text += str(i)+"|"+str(j)+" "
        end = time.time()
        st.write(_text)
        st.write()
        st.write("Running times: "+str(end - start))

st.write("See the documentation at [pos_tag | PyThaiNLP](https://pythainlp.github.io/docs/3.0/api/tag.html#pythainlp.tag.pos_tag).")
