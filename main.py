import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

# Function to convert text to speech and play the audio
def speak(text):
    # Create a Text-to-Speech (TTS) object with the provided text and language set to English
    tts = gTTS(text=text, lang="en")
    
    # Define the filename where the generated audio will be saved
    filename = "voice.mp3"
    
    # Save the generated speech audio as an MP3 file
    tts.save(filename)
    
    # Play the saved audio file
    playsound.playsound(filename)

# Call the speak function with a greeting message
speak("Hey there! I am your personal Voice Assistant.")