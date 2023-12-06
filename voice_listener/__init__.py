import speech_recognition as sr
from vocal_command import VocalCommandInvoker
from text_to_speech import synthesize_speech

__recognizer = sr.Recognizer()
__command_invoker = VocalCommandInvoker()
__green = '\033[92m'
__reset = '\033[0m'


def __input_microphone_index(max_index: int) -> int:
    str_choice = input("Enter the number of the microphone you want to use:")
    try:
        choice = int(str_choice)
        if max_index < choice and choice >= 0:
            print(f"The number must be between 0 and {max_index - 1}")
            return __input_microphone_index(max_index)
        else:
            return choice
    except ValueError:
        print("Error, try again")
        return __input_microphone_index(max_index)


def choose_microphone() -> int | None:
    microphone_names = sr.Microphone.list_microphone_names()
    if microphone_names:
        index = 0

        for microphone_name in microphone_names:
            print(microphone_name + " index: " + str(index))
            index += 1
        return __input_microphone_index(max_index=index)
    else:
        print("No microphone detected.")
        return None


def capture_voice_input() -> None:
    microphone_index = choose_microphone()
    synthesize_speech("Bonjour ! Comment puis-je vous aider ?")

    with sr.Microphone(device_index=microphone_index) as source:
        while True:
            audio_data = __recognizer.listen(source)
            text_data = convert_voice_to_text(audio_data=audio_data)
            print(__green + "Vous : " + text_data + __reset)
            if text_data:
                __command_invoker.run_command(data=text_data)


def convert_voice_to_text(audio_data: sr.AudioData) -> str:
    text: str = ""
    try:
        text = __recognizer.recognize_google(audio_data, language="fr-FR")
    except sr.UnknownValueError:
        synthesize_speech("Désolé, je n'ai pas compris.")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
    return text
