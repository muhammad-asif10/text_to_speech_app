import streamlit as st
import pyttsx3
import os

st.set_page_config(
    page_title="TTS",
    page_icon="🎙️",
    layout="centered"
)
st.title("Text to Speech")
text = st.text_area("Type text and click the Speak button to hear it.", height=100)

# Initialize engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_names = [voice.name for voice in voices]

selected_voice_name = st.selectbox("Select Voice", voice_names, index=0)

# Find the ID for the selected voice name
selected_voice_id = None
for v in voices:
    if v.name == selected_voice_name:
        selected_voice_id = v.id
        break

col1, col2 = st.columns(2)
with col1:
    rate = st.slider("Speed", 50, 200, 100)  
with col2:
    volume = st.slider("Volume", 0.0, 1.0, 0.5)

# Speak button
if st.button("Generate Audio"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            # Configure engine
            engine.setProperty('voice', selected_voice_id)
            engine.setProperty('rate', rate)
            engine.setProperty('volume', volume)
            
            # SAVE TO FILE instead of .say()
            output_file = "speech.mp3"
            engine.save_to_file(text, output_file)
            engine.runAndWait()
            
            # Display audio player in browser
            st.audio(output_file, format="audio/mp3")
            st.success("Audio generated successfully!")
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer (Keeping your original styling)
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
