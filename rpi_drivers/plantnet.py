import requests
import json
from pprint import pprint

from .api_key import API_KEY   # Your API key here
PROJECT = "all"; # You can choose a more specific flora, see: /docs/newfloras

class PlantNet:
    def __init__(self):
        self.api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

        self.data = { 'organs': ['auto'] }

    def send_multiple_requests(self, lst_images):
        results = []
        for img in lst_images:
            result = self.send_request(img)
            results.append(result)
        return results

    def send_request(self, image):
        files = [
            ('images', ("/home/jufo", image))
        ]

        req = requests.Request('POST', url=self.api_endpoint, files=files, data=self.data)
        prepared = req.prepare()

        s = requests.Session()
        response = s.send(prepared)
        json_result = json.loads(response.text)

        bestMatch = json_result['bestMatch']

        with open('latest_data.json', 'w', encoding='utf-8') as file:
            json.dump(json_result, file, ensure_ascii=False, indent=4)

        return bestMatch
