import streamlit as st
import requests

# Streamlit UI
st.title("Audio to Text Summarization")

# Upload audio file
audio_file = st.file_uploader("Upload Audio File", type=["mp3", "wav"])

if audio_file:
    # Convert audio to text using Faster Whisper (or other audio-to-text model)
    # Here you would call your audio-to-text model

    # For demo purposes, let's assume text is extracted from audio
    text_from_audio = "This is the text extracted from the audio."

    # Send text to FastAPI backend for summarization
    backend_url = "http://localhost:8000/summarize"  # Update with your backend URL
    payload = {"text": text_from_audio}
    response = requests.post(backend_url, json=payload)

    # Display summarized text
    if response.status_code == 200:
        summarized_text = response.json()["summary"]
        st.header("Summarized Text:")
        st.write(summarized_text)
    else:
        st.error("Failed to summarize text. Please try again.")
