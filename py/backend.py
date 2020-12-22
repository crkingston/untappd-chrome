import requests
import os

from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv("CLIENTID")
client_secret = os.getenv("CLIENTSECRET")

payload = {'client_id': client_id, 'client_secret': client_secret}
url = 'https://api.untappd.com/v4'
method = '/beer/info/452240'
url_method = url + method
r = requests.get(url_method, params=payload)

print(r.url)
print(r.text)
