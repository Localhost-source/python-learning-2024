# requests is the python library to hit the external APIs
import requests # type: ignore

api_url = "https://dummyapi.online/api/movies"


response = requests.get(api_url)

print(response.status_code)
print(response.text)
print(response.json())

print(dir(response))
print(response.headers)


a = 2
print(dir(a))