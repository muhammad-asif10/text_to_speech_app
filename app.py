import streamlit as st
import pyttsx3

st.set_page_config(
    page_title="TTS",
    page_icon="🎙️",
    layout="centered"
)
st.title("Text to Speech")
text = st.text_area("Type text and click the Speak button to hear it.", height=100)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Create a dictionary of voice_name: voice_id
voice_names = [voice.name for voice in voices]

selected_voice_name = st.selectbox("Select Voice", voice_names, index=0)
selected_voice = next((v for v in voices if v.name == selected_voice_name), None)

col1, col2 = st.columns(2)
with col1:
    rate = st.slider("Speed", 50, 100, 200)  # default 100
with col2:
    volume = st.slider("Volume", 0.0, 0.5, 1.0)

# Speak button
if st.button("Speak"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        engine.setProperty('voice', selected_voice_name)
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        engine.say(text)
        engine.runAndWait()

st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f5f7fa;
    color: #555;
    text-align: center;
    padding: 8px;
    font-size: 12px;
    border-top: 1px solid #ddd;
}
</style>

<div class="footer">
Muhammad Asif | University of Veterinary & Animal Sciences (UVAS), Ravi Campus
</div>
""", unsafe_allow_html=True)
