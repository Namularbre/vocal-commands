import voice_listener
from dotenv import load_dotenv
from os import getenv


if __name__ == "__main__":
    if load_dotenv():
        try:
            if getenv("MICROPHONE_INDEX"):
                microphone_index = int(getenv("MICROPHONE_INDEX"))
            else:
                microphone_index = 0
            voice_listener.capture_voice_input(microphone_index=microphone_index)
        except KeyboardInterrupt:
            exit(0)
    else:
        print("Error: .env file is not found")
