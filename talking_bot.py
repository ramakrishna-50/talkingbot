"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

import pyttsx3

import google.generativeai as genai

genai.configure(api_key="AIzaSyCjhXKKta38Uk1GqdINRa90boQ62Odt-fI")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please say something... (listening for 5 seconds)")

    # Adjust for ambient noise and record the audio for 5 seconds
    recognizer.adjust_for_ambient_noise(source)
    try:
        #audio = recognizer.listen(source, timeout=5)

        # Use Google's speech recognition
        text = "what is the purpose of life"
        print("You said: " + text)

        inst = "Instruction: Talk like lord sai baba and Respond with wisdom as god to baktha."
        question = inst+text
        response = chat_session.send_message(question)

        print(response.text)

        engine = pyttsx3.init()
        engine.say(response.text)
        engine.runAndWait()
    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Web Speech API; check your network connection.")





