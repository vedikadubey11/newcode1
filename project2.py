import requests  
import json  
  
def get_weather(api_key, city, country_code):  
   base_url = "http://api.openweathermap.org/data/2.5/weather"  
   params = {  
      "q": f"{city},{country_code}",  
      "appid": api_key,  
      "units": "metric"  
   }  
   response = requests.get(base_url, params=params)  
   weather_data = response.json()  
   return weather_data  
  
def print_weather(weather_data):  
   print("Current Weather:")  
   print(f"City: {weather_data['name']}")  
   print(f"Temperature: {weather_data['main']['temp']}°C")  
   print(f"Humidity: {weather_data['main']['humidity']}%")  
   print(f"Weather Condition: {weather_data['weather']['description']}")  
  
def main():  
   api_key = "YOUR_OPENWEATHERMAP_API_KEY"  
   city = "London"  
   country_code = "UK"  
   weather_data = get_weather(api_key, city, country_code)  
   print_weather(weather_data)  
  
if __name__ == "__main__":  
   main()
