import requests

class BaseApiRequest():
    async def get_data(self, url: str) -> str | None:
        response = requests.get(url)
        if response.ok:
            return response.json()
        else:
            return None