import speech_recognition as sr


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


def write_in_dotenv(microphone_index: int) -> None:
    with open('./.env', 'a') as dotenv:
        dotenv.write(f"MICROPHONE_INDEX={microphone_index}")
