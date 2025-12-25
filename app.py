import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
import tempfile
import io
import sys
import os

# -----------------------
# FFmpeg setup (Windows only)
# -----------------------
if sys.platform.startswith("win"):
    ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg", "bin", "ffmpeg.exe")
    if os.path.exists(ffmpeg_path):
        AudioSegment.converter = ffmpeg_path

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="English TTS",
    page_icon="🎙️",
    layout="centered",
)

st.title("Text to Speech (English Only)")

# -----------------------
# Text input
# -----------------------
text = st.text_area("Type text and click the Speak button to hear it.", height=100)

# -----------------------
# Sliders for speed & volume
# -----------------------
col1, col2 = st.columns(2)
with col1:
    speed = st.slider("Speed (0.5 = slow, 2.0 = fast)", 0.5, 2.0, 1.0, step=0.1)
with col2:
    volume = st.slider("Volume (-20dB to +20dB)", -20, 20, 0, step=1)

# -----------------------
# Speak button
# -----------------------
if st.button("🎙️ Speak"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        tts = gTTS(text=text, lang="en")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts.save(tmp_file.name)
            audio = AudioSegment.from_file(tmp_file.name)

        # Adjust volume
        audio = audio + volume

        # Adjust speed
        new_frame_rate = int(audio.frame_rate * speed)
        audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_frame_rate})
        audio = audio.set_frame_rate(44100)

        # Export to BytesIO
        audio_bytes = io.BytesIO()
        audio.export(audio_bytes, format="mp3")
        st.audio(audio_bytes.getvalue(), format="audio/mp3")

# -----------------------
# Footer
# -----------------------
st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)