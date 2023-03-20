"""
import pyttsx3

voiceoverDir = "Voiceovers"

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 125)
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(text, filePath)
    engine.runAndWait()
    return filePath
"""


from TTS.api import TTS

voiceoverDir = "Voiceovers"

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    tts.tts_to_file(text=text,file_path=filePath)
    return filePath

