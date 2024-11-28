import requests

def get_weather(city, api_key):
    url =  f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        city_name = data['name']
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather.capitalize()}")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data : {e}")
    except KeyError:
        print("Invalid city name or API response")

if __name__ == "__main__":
    api_key = "7dc699f18659531149e35564315cd04d" # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    get_weather(city, api_key)

