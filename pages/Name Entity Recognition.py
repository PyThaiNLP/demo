import streamlit as st
import time
from pythainlp.tag import NER

st.markdown("""
# Name Entity Recognition

PyThaiNLP support Name Entity Recognition. We have
- thainer - Thai NER engine
- wangchanberta* - wangchanberta model
- tltk - wrapper for TLTK

and trained with corpus

- thainer - Thai NER corpus
- lst20 - lst20 corpus (wangchanberta only)

**Note**: for tltk engine, It's support ner model from tltk only.
""")

_engine =None
with st.form("my_form"):
    st.write("Inside the form")
    text = st.text_area("text")
    engine=st.selectbox('Select engine', ['thainer', 'wangchanberta', 'tltk'], key=1,index=0)
    corpus=st.selectbox('Select corpus', ['thainer', 'lst20'], key=1,index=0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.subheader("Tags: ")
        _engine = NER(engine=str(engine), corpus=str(corpus))
        st.write(_engine.tag(text,tag=True))

st.write("See the documentation at [NER | PyThaiNLP](https://pythainlp.github.io/docs/3.0/api/tag.html#pythainlp.tag.NER).")
