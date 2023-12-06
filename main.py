import voice_listener
from dotenv import load_dotenv


if __name__ == "__main__":
    if load_dotenv():
        try:
            voice_listener.capture_voice_input()
        except KeyboardInterrupt:
            exit(0)
    else:
        print("Error: .env file is not found")
