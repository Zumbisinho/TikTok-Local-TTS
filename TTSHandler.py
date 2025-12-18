from gtts import gTTS
from pydub import AudioSegment
from io import BytesIO

def SayText(text:str,lang:str):
    fp = BytesIO()
    wav_fp = BytesIO()
    tts = gTTS(lang=lang,text=text)
    tts.write_to_fp(fp)
    fp.seek(0)
    sound = AudioSegment.from_file(fp)
    wav_fp = sound.export(fp, format = "wav")
    return wav_fp