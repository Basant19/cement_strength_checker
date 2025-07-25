
import requests

url = "http://54.88.209.1:8080/"

try:
    response = requests.get(url, timeout=5)
    print("✅ Status Code:", response.status_code)
    print("✅ Response Body:", response.text[:200])  # print first 200 chars
except requests.exceptions.RequestException as e:
    print("❌ Error connecting to the app:", e)
