import requests
import json
import time
import random

# API URL
API_URL = "https://demo.xcf5.com/api"

# Payload options
payloads = [
    {"serviceName": "creditcard"},
    {"serviceName": "ssn"}
]

def send_request():
    """Sends a request to the API with a random serviceName."""
    payload = random.choice(payloads)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)

        # Print raw response
        print(f"Sent: {payload} | Status Code: {response.status_code} | Raw Response: {response.text}")

        if response.status_code != 200:
            print("Warning: Non-200 status code received.")
            return

        # Attempt JSON parsing safely
        try:
            json_response = response.json()
            print(f"Parsed Response: {json_response}")
        except json.JSONDecodeError:
            print("Error: Response is not valid JSON.")

    except Exception as e:
        print(f"Error sending request: {e}")

# Run in a loop to generate continuous traffic
if __name__ == "__main__":
    while True:
        send_request()
        time.sleep(random.uniform(0.5, 2))  # Random delay between 0.5s - 2s

