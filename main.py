import requests

def get_weather(city):
    api_key = 'your_api_key'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    try:
        response = requests.get(url)
        response_json = response.json()
        if response.status_code == 200:
            with open('weather.txt', 'w', encoding='utf-8') as file:
                file.write(f'City: {response_json['name']}\n')
                file.write(f'Temperature: {response_json['main']['temp']}°C\n')
                file.write(f'Description: {response_json['weather'][0]['description'].capitalize()}\n')
                file.write(f'Humidity: {response_json['main']['humidity']}%\n')
                file.write(f'Wind speed: {response_json['wind']['speed']} m/s\n')
                file.write(f'Feels like: {response_json['main']['feels_like']}°C\n')
                file.write(f'Pressure: {response_json['main']['pressure']} hPa\n')
        else:
            return 'Error!'
    except requests.exceptions.RequestException as e:
        return f'Network error: {e}'
    except KeyError:
        return 'Unexpected API response. Please check your inputs'
    except ValueError:
        return 'Please enter a valid city'

try:
    city = input('Enter a city: ')
    get_weather(city=city)
except ValueError:
    print('Invalid input. Please enter a numeric value for the city')
