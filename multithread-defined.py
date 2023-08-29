import requests
import json
import threading

def send_request(url, payload, request_num):
    response = requests.post(url, headers=headers, data=payload)
    print("Request ke", request_num, "Response Target", url, "adalah =", response.status_code)

url = "API_ENDPOINT"

payload = "PAYLOAD_GOES_HERE"

headers = {
    'Content-Type': 'application/json'
}

initial_val = 1
num_requests = 1000 

threads = []
for i in range(initial_val, initial_val + num_requests):
    thread = threading.Thread(target=send_request, args=(url, payload, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
