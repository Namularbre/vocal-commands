import requests


def http_get(url: str, params=None) -> str | None:
    if params is None:
        params = {}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error while fetching ressource {url}: {response.status_code} -> {response.text}")
        return None
