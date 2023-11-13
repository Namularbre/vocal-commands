import speech_recognition as sr

from logger import logger
from vocal_command import VocalCommandInvoker
from text_to_speech import synthesize_speech

__recognizer = sr.Recognizer()
__command_invoker = VocalCommandInvoker()


def capture_voice_input() -> None:
    synthesize_speech("Bonjour ! Comment puis-je vous aidez ?")
    with sr.Microphone(device_index=1) as source:
        while True:
            audio_data = __recognizer.listen(source)
            text_data = convert_voice_to_text(audio_data=audio_data)
            logger.info("What the application understood: " + text_data)
            if text_data:
                __command_invoker.run_command(data=text_data)


def convert_voice_to_text(audio_data: sr.AudioData) -> str:
    text: str = ""
    try:
        text = __recognizer.recognize_google(audio_data, language="fr-FR")
    except sr.UnknownValueError:
        synthesize_speech("Désolé, je n'ai pas compris.")
    except sr.RequestError as e:
        logger.critical("Error; {0}".format(e))
    return text
