import webbrowser
from os import getenv


def search_on_browser(query: str) -> None:
    web_browser_path = getenv("WEB_BROWSER_PATH")
    search_url = "https://www.google.com/search?q=" + query.strip()
    try:
        if web_browser_path:
            webbrowser.register('web_browser', None, webbrowser.BackgroundBrowser(web_browser_path))
            webbrowser.get('web_browser').open_new_tab(search_url)
        else:
            webbrowser.open(search_url)
    except FileNotFoundError as e:
        print(f"Unable to open web browser with path {web_browser_path} : {e}")
