import streamlit as st
import time
from pythainlp.soundex import soundex
st.markdown("""
# Soundex 🎉

PyThaiNLP support Soundex for searching or indexing. We have

- udom83 (default) - Thai soundex algorithm proposed by Vichit Lorchirachoonkul.
- lk82 - Thai soundex algorithm proposed by Wannee Udompanich.
- metasound - Thai soundex algorithm based on a combination of Metaphone and Soundex proposed by Snae & Brückner.

for this demo page.
""")

with st.form("my_form"):
    st.write("Inside the form")
    text = st.text_area("text")
    engine=st.selectbox('Select soundex', ['udom83', 'lk82', 'metasound'], key=1,index=0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.subheader("Soundex: ")
        start = time.time()
        for i in str(text).splitlines():
            _temp = soundex(str(i), engine=str(engine))
            st.write(_temp)
        end = time.time()
        st.write()
        st.write("Running times: "+str(end - start))

st.markdown("See the documentation at [https://pythainlp.github.io/docs/3.0/api/soundex.html](https://pythainlp.github.io/docs/3.0/api/soundex.html).")
# st.sidebar.markdown("# Soundex 🎉")
