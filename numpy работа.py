import requests

# Set API endpoint and parameters
url = "http://api.weatherapi.com/v1/current.json"
params = {
    "q": "Moscow",
    "key": "1f4fe04d817a4c43bc5143724240606"
}

# Send GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print("Текущая погода в Москве:")
    print(f"Температура: {data['current']['temp_c']}°C")
    print(f"Влажность: {data['current']['humidity']}%")
else:
    print("Не удалось получить данные")