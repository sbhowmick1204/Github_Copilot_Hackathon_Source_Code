# Github_Copilot_Hackathon_Source_Code

The program is a Python script that uses the OpenWeatherMap API to fetch weather information for a given city. Here's a breakdown of the main concepts and logic used in the program:

Importing Modules:

The script begins by importing the requests module for making HTTP requests and the json module for working with JSON data.

API Key and Limit:

The API_KEY variable stores the API key required to access the OpenWeatherMap API. You need to replace this with your own valid API key.
The limit variable specifies the maximum number of results to retrieve when searching for the latitude and longitude of a city.

get_lat_long(city) Function:

This function takes a city name as input and uses the OpenWeatherMap API to fetch the latitude and longitude of the city.
It constructs a URL with the API key, city name, and limit and sends a GET request to the API.
If the request is successful (status code 200), the response is converted to JSON format.
If the response contains data, the latitude and longitude are extracted from the first result and returned. Otherwise, None is returned.
Exception handling is implemented to handle connection errors.

get_weather(city, latitude, longitude) Function:

This function takes a city name, latitude, and longitude as input and uses the OpenWeatherMap API to fetch weather data for the specified location.
It constructs a URL with the latitude, longitude, API key, and units (metric for Celsius) and sends a GET request to the API.
If the request is successful, the response is converted to JSON format and returned. Otherwise, None is returned.
Exception handling is implemented to handle connection errors.

main() Function:

This is the main function that interacts with the user and calls the other functions.
It prompts the user to enter a city name and calls get_lat_long() to fetch the latitude and longitude.
If the latitude and longitude are obtained, it calls get_weather() to fetch weather data for that location.
If the weather data is available, it prints various weather parameters such as temperature, humidity, wind speed, etc.
The function also includes a loop to allow the user to search for weather multiple times until they choose to quit.

Program Execution:

The script checks if it is being executed directly (_name_ == '_main_') and starts the main loop.
The user is prompted to enter a city name, and the weather information is displayed if available.
After displaying the weather, the user is given the option to search again. If they choose not to, the loop breaks, and the program ends.

Overall, the program uses the OpenWeatherMap API to retrieve the latitude and longitude of a city and then uses those coordinates to fetch the weather information for that location. It provides a basic command-line interface for the user to search for weather data for different cities.
