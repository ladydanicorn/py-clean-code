class UserInterface:
    def __init__(self, data_fetcher, parser):
        self.data_fetcher = data_fetcher
        self.parser = parser

    def display_weather(self, city):
        data = self.data_fetcher.fetch(city)
        weather_report = self.parser.parse(data)
        print(weather_report)

    def get_detailed_forecast(self, city):
        data = self.data_fetcher.fetch(city)
        return self.parser.parse(data)

    def run(self):
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