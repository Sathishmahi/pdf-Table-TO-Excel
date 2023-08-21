import requests

def get_public_ip():
    try:
        response = requests.get("https://httpbin.org/ip")
        if response.status_code == 200:
            data = response.json()
            return data.get("origin")
        else:
            return "Error: Unable to retrieve IP address."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

public_ip = get_public_ip()
print(f"Public IP Address: {public_ip}")
