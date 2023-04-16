from google.cloud import texttospeech
from playsound import playsound
from utils import components

import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_cloud_credentials.json'

# Setup text-to-speech configuration
client = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Studio-M")
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16, pitch=0)

def _save_speech_to_file(text, audio_file_path):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(audio_file_path, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)


def speak(text):
    if text is None:
        return
    audio_file_path = "output.wav"

    _save_speech_to_file(text, audio_file_path)
    components.move_mouth_servo()
    playsound(audio_file_path)
    components.stop_mouth_servo()