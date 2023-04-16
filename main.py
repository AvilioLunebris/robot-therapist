from utils import microphone
from utils import chatgpt
from utils import tts
from utils import components

from signal import pause

def start():
    speech = microphone.get_speech()
    chatgpt_response = chatgpt.get_response(speech)
    tts.speak(chatgpt_response)
    
components.push_to_talk_button.when_pressed = start
pause() # Keep script running
