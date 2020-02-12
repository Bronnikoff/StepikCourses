import requests
import sys

url = sys.argv[1]

try:
    result = requests.get(url, timeout = 20)
    result.raise_for_status()
except requests.Timeout:
    print(url, "not answer")
except requests.HTTPError as err:
    print(url, "returns error with code:", err.response.status_code)
except requests.RequestException:
    print("requests ended with unknown error")
else:
    print("--------------------------------------------")
    print(result.headers)
    print("--------------------------------------------")
