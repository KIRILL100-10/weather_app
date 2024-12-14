import requests

def get_weather(city):
    api_key = '35cf7e4f317c014b92ea8cf0f7b02fd4'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response_json = response.json()
            print(f'City: {response_json['name']}')
            print(f'Temperature: {response_json['main']['temp']}°C')
            print(f'Description: {response_json['weather'][0]['description'].capitalize()}')
            print(f'Humidity: {response_json['main']['humidity']}%')
            print(f'Wind speed: {response_json['wind']['speed']} m/s')
            print(f'Feels: {response_json['main']['feels_like']}°C')
            print(f'Pressure: {response_json['main']['pressure']} hPa')
    except:
        print('Error!')

city = input('Enter a city: ')
get_weather(city=city)
