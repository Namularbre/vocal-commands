import webbrowser
from logger import logger
from dotenv import env


def search_on_browser(query: str) -> None:
    firefox_path = env["WEB_BROWSER_PATH"]
    search_url = "https://www.google.com/search?q=" + query.strip()
    try:
        if firefox_path:
            webbrowser.register('web_browser', None, webbrowser.BackgroundBrowser(firefox_path))
            webbrowser.get('web_browser').open_new_tab(search_url)
        else:
            webbrowser.open_new_tab(search_url)
        logger.info(f"Web browser open on {search_url}")
    except FileNotFoundError as e:
        logger.critical(f"Unable to open web browser with path {firefox_path} : {e}")
