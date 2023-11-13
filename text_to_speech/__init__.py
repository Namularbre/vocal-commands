from gtts import gTTS
from mp3_player import read_audio_file


def synthesize_speech(text: str) -> None:
    tts = gTTS(text=text, lang="fr")
    tts.save("response.mp3")
    read_audio_file("response.mp3")
