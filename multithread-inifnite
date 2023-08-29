import requests
import json
import threading

def send_request(url, payload):
    response = requests.post(url, headers=headers, data=payload)
    print("Request sent to", url, "Response status code:", response.status_code)

url = "API_ENDPOINT"

payload = "PAYLOAD_GOES_HERE"

headers = {
    'Content-Type': 'application/json'
}

while True:
    thread = threading.Thread(target=send_request, args=(url, payload))
    thread.start()
