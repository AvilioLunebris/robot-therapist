import speech_recognition as sr
from playsound import playsound

recognizer = sr.Recognizer()

def get_speech():
    with sr.Microphone() as source:
        playsound("sound_effects/bell.wav", block=False)
        
        try:
            # Record speech
            audio_data = recognizer.listen(source, timeout=4)

            # Convert speech to text
            text = recognizer.recognize_google(audio_data)
        except Exception as e:
            print(e)
            return None
        
        playsound("sound_effects/success.wav")
        return text