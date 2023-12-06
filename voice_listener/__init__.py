import speech_recognition as sr
from vocal_command import VocalCommandInvoker
from text_to_speech import synthesize_speech

__recognizer = sr.Recognizer()
__command_invoker = VocalCommandInvoker()
__green = '\033[92m'
__reset = '\033[0m'


def capture_voice_input(microphone_index: int = 0) -> None:
    synthesize_speech("Bonjour ! Comment puis-je vous aider ?")

    with sr.Microphone(device_index=microphone_index) as source:
        while True:
            audio_data = __recognizer.listen(source)
            text_data = __convert_voice_to_text(audio_data=audio_data)
            print(__green + "Vous : " + text_data + __reset)
            if text_data:
                __command_invoker.run_command(data=text_data)


def __convert_voice_to_text(audio_data: sr.AudioData) -> str:
    text: str = ""
    try:
        text = __recognizer.recognize_google(audio_data, language="fr-FR")
    except sr.UnknownValueError:
        synthesize_speech("Désolé, je n'ai pas compris.")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
    return text
