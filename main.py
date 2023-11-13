import voice_listener

if __name__ == "__main__":
    try:
        voice_listener.capture_voice_input()
    except KeyboardInterrupt:
        exit(0)
