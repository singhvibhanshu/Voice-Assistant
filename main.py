# Import necessary modules
import os  # For operating system related tasks (not used in this example but imported)
import time  # For handling time-related operations (not used in this example but imported)
import playsound  # For playing audio files
import speech_recognition as sr  # For speech recognition
from gtts import gTTS  # For text-to-speech conversion

# Function to convert text to speech and play the audio
def speak(text):
    """
    Converts the input text into speech, saves it as an audio file, and plays it.
    Args:
        text (str): The text to be converted into speech.
    """
    # Create a Text-to-Speech (TTS) object with the provided text and language set to English
    tts = gTTS(text=text, lang="en")
    
    # Define the filename where the generated audio will be saved
    filename = "voice.mp3"
    
    # Save the generated speech audio as an MP3 file
    tts.save(filename)
    
    # Play the saved audio file
    playsound.playsound(filename)


# Function to capture audio input from the microphone and convert it to text
def get_audio():
    """
    Listens to audio input from the microphone, processes it, and converts it into text.
    Returns:
        str: The text obtained from the speech input. Returns an empty string if an error occurs.
    """
    # Initialize the Recognizer instance for speech recognition
    r = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")  # Notify the user that the system is listening
        audio = r.listen(source)  # Capture the audio input
        
        said = ""  # Variable to store the recognized text

        try:
            # Use Google Web Speech API to recognize the audio input
            said = r.recognize_google(audio)
            print("You said:", said)  # Print the recognized text
        except Exception as e:
            # Print an error message if speech recognition fails
            print("Exception:", str(e))

    return said  # Return the recognized text


# Call the speak function with a greeting message
speak("Hey there! I am your personal Voice Assistant.")

# Capture and print the user's speech input
get_audio()