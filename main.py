import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
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


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()