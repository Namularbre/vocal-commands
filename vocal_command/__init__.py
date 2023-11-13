from abc import ABC, abstractmethod

from text_to_speech import synthesize_speech
from weather_reporter import get_weather
from web_searcher import search_on_browser


class VocalCommand(ABC):
    def __init__(self, name: str, description: str) -> None:
        self.__name = name
        self.__description = description

    def is_called(self, text: str) -> bool:
        return self.__name in text

    def name(self) -> str:
        return self.__name

    @abstractmethod
    def run(self, data: str | None = None) -> None:
        pass


class VocalCommandInvoker:
    def __init__(self) -> None:
        self.__commands: list = []
        self.__commands.append(HelloCommand())
        self.__commands.append(HelloCommand())
        self.__commands.append(WeatherCommand())
        self.__commands.append(RepeatCommand())
        self.__commands.append(SearchCommand())
        self.__stop_command = StopCommand()

    def run_command(self, data: str | None = None) -> None:
        command_ran = False
        for command in self.__commands:
            if self.command_name_match_first_word(command, data):
                command.run(data)
                command_ran = True
                break
        if not command_ran and self.__stop_command.name() in data.lower():
            self.__stop_command.run()

    def command_name_match_first_word(self, command: VocalCommand, data: str) -> bool:
        return command.name() in data.lower().split(" ")[0]


class HelloCommand(VocalCommand):
    def __init__(self) -> None:
        super().__init__(name="bonjour", description="Vous répond bonjour.")

    def run(self, data: str | None = None) -> None:
        synthesize_speech("Bonjour !")


class StopCommand(VocalCommand):
    def __init__(self) -> None:
        super().__init__(name="au revoir", description="Ferme le programme.")

    def run(self, data: str | None = None) -> None:
        synthesize_speech("Au revoir, à bientôt !")
        exit(0)


class WeatherCommand(VocalCommand):
    def __init__(self) -> None:
        super().__init__(name="météo", description="Donne la météo actuel de Limoges.")

    def run(self, data: str | None = None) -> None:
        weather = get_weather()
        synthesize_speech(weather)


class SearchCommand(VocalCommand):
    def __init__(self) -> None:
        super().__init__(name="cherche", description="Ouvre le navigateur spécifié dans le ficher .env avec ce que "
                                                     "vous souhaitez chercher")

    def run(self, data: str | None = None) -> None:
        text = data.lower().split("cherche")[1]
        search_on_browser(text)
        synthesize_speech(f"Recherche pour {text} lancée")


class RepeatCommand(VocalCommand):
    def __init__(self) -> None:
        super().__init__(name="répète", description="Répète ce que vous dite")

    def run(self, data: str | None = None) -> None:
        synthesize_speech(data.replace("répète ", ""))
