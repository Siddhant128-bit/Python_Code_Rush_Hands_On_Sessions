import requests
from pathlib import Path

url = 'http://127.0.0.1:8000/upload/'
image_path = Path(input('Enter the path of the image: '))

files = {'image': open(image_path, 'rb')}
response = requests.post(url, files=files)
print(response.text)

