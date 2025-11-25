import requests
import json
from pprint import pprint

API_KEY = "2b10tWgZKbjcm1jfLM3W4v0qk"   # Your API key here
PROJECT = "all"; # You can choose a more specific flora, see: /docs/newfloras
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

image_path_1 = r"./data/Bild1.png"
image_data_1 = open(image_path_1, 'rb')

image_path_2 = r"./data/Bild2.png"
image_data_2 = open(image_path_2, 'rb')

data = { 'organs': ['auto'] }

files = [
  ('images', (image_path_2, image_data_2))
]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)

bestMatch = json_result['bestMatch']
if bestMatch.lower().find('arabidopsis') == -1:
    print("no arabidopsis")
    print(bestMatch)
else:
    print(bestMatch)
    pprint(json_result)

with open('latest_data.json', 'w', encoding='utf-8') as file:
    json.dump(json_result, file, ensure_ascii=False, indent=4)
