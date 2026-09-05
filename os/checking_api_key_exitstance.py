import os

api_key = os.environ.get("API_KEY")

if api_key is not None:
    print("API key found")
else:
    print("API key not found")