import requests

def get_weather(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    try:
        response = requests.get(url)
        response_json = response.json()
        if response.status_code == 200:
            print(f'City: {response_json['name']}')
            print(f'Temperature: {response_json['main']['temp']}°C')
            print(f'Description: {response_json['weather'][0]['description'].capitalize()}')
            print(f'Humidity: {response_json['main']['humidity']}%')
            print(f'Wind speed: {response_json['wind']['speed']} m/s')
            print(f'Feels like: {response_json['main']['feels_like']}°C')
            print(f'Pressure: {response_json['main']['pressure']} hPa')
        else:
            return 'Error!'
    except requests.exceptions.RequestException as e:
        return f'Network error: {e}'
    except KeyError:
        return 'Unexpected API response. Please check your inputs'
    except ValueError:
        return 'Please enter a valid city'
try:
    api_key = input('Enter an API key: ')
    city = input('Enter a city: ')
    get_weather(city=city, api_key=api_key)
except ValueError:
    print('Invalid input. Please enter a numeric value for the city')
