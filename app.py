import streamlit as st
from gtts import gTTS
import os

st.set_page_config(
    page_title="TTS",
    page_icon="🎙️",
    layout="centered"
)

st.title("Text to Speech")

text = st.text_area(
    "Type text and click the button to generate audio",
    height=120
)

language = st.selectbox(
    "Select Language",
    ["en", "ur", "hi", "ar"],
    index=0
)

if st.button("Generate Audio"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            tts = gTTS(text=text, lang=language)
            output_file = "speech.mp3"
            tts.save(output_file)

            st.audio(output_file, format="audio/mp3")
            st.success("Audio generated successfully!")

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("""
<style>
.footer {
    position: fixed; left: 0; bottom: 0; width: 100%;
    background-color: #f5f7fa; color: #555; text-align: center;
    padding: 8px; font-size: 12px; border-top: 1px solid #ddd;
}
</style>
<div class="footer">
Muhammad Asif | University of Veterinary & Animal Sciences (UVAS), Ravi Campus
</div>
""", unsafe_allow_html=True)
