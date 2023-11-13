import os
import pygame
from logger import logger


def read_audio_file(file_name: str) -> None:
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        logger.critical(f"Error {e}")
    finally:
        pygame.mixer.quit()
        __remove_audio_file(file_name)


def __remove_audio_file(file_name: str) -> None:
    try:
        os.remove(file_name)
    except FileNotFoundError:
        logger.critical(f"Unable to remove nonexistent file {file_name}")
