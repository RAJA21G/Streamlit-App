
import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Set the title of the app
st.title("Language Translator")

# Dropdown for source language selection
src_lang = st.selectbox("Select Source Language", list(LANGUAGES.values()), index=0)

# Dropdown for target language selection
target_lang = st.selectbox("Select Target Language", list(LANGUAGES.values()), index=1)

# Text input for user to enter text to translate
text_to_translate = st.text_area("Enter text to translate:", "")

# Button to perform translation
if st.button("Translate"):
    if text_to_translate:
        # Perform the translation
        translated = translator.translate(text_to_translate, src=list(LANGUAGES.keys())[list(LANGUAGES.values()).index(src_lang)], dest=list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_lang)])
        st.success(f"Translated Text: {translated.text}")
    else:
        st.warning("Please enter text to translate.")

# Show available languages for reference
st.sidebar.header("Available Languages")
for lang_code, lang_name in LANGUAGES.items():
    st.sidebar.write(f"{lang_code}: {lang_name}")
