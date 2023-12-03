import voice_listener
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    try:
        voice_listener.capture_voice_input()
    except KeyboardInterrupt:
        exit(0)
