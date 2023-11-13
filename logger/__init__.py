import os
from datetime import datetime
from dotenv import env

development_setting: str = env["RUN_MOD"]


class AlexandrieLogger:
    def __init__(self):
        self.__mode = None

    def set_debug_mode(self, debug_mode: str):
        self.__mode = debug_mode

    def info(self, message: str) -> None:
        if self.__is_debug_mode():
            print("Info:", message)

    def debug(self, message: any) -> None:
        if self.__is_debug_mode():
            print("Debug:", message)

    def critical(self, message: str) -> None:
        if self.__is_debug_mode():
            print("Error:", message)

    def __is_debug_mode(self) -> bool:
        return self.__mode.lower() == "debug"

    def __write_log(self, data: any) -> None:
        __workdir = os.getcwd().replace('\\\\', '/')
        __filename = f"{__workdir}/logs/alexandrie{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}"
        with open(__filename, 'a', encoding="utf-8") as log_file:
            log_file.write(str(data))


logger: AlexandrieLogger = AlexandrieLogger()
logger.set_debug_mode(debug_mode=development_setting)
