class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch(self, city):
        # Retrieves data for a specific city or returns an empty dictionary if not found
        return self.weather_data.get(city, {})





# user_interface.py
class UserInterface:
    def __init__(self, data_fetcher, parser):
        self.data_fetcher = data_fetcher
        self.parser = parser

    def display_weather(self, city):
        # Fetches and displays basic weather data
        data = self.data_fetcher.fetch(city)
        weather_report = self.parser.parse(data)
        print(weather_report)

    def get_detailed_forecast(self, city):
        # Could be extended for more detailed forecast data handling
        data = self.data_fetcher.fetch(city)
        return self.parser.parse(data)

    def run(self):
        # Main loop for the user interaction
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)
