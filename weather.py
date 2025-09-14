import requests

def get_weather(city):
    API_KEY = "59a32b5e742d3ca8ad2f5cd18b2004d8"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

    # Build full URL
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            humidity = main["humidity"]
            description = weather["description"]

            print(f"\n🌍 Weather in {city.capitalize()}:")
            print(f"🌡 Temperature: {temperature}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"☁ Condition: {description.capitalize()}")
        else:
            print("❌ City not found. Please enter a valid city name.")

    except Exception as e:
        print("⚠ Error fetching data:", e)

# --- Main program ---
if __name__=="__main__":
    city = input("Enter city name: ")
    get_weather(city)
