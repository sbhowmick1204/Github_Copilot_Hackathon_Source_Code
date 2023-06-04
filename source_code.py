import requests    # importing the requests module to send a request to the url
import json        # importing the json module to convert the response to json format

#variable to save the API key
API_KEY= '8fb8cf48ddcb7268d1b9e3cd79dc8718'
limit=5       #limit to get the latitude and longitude of a city

#function to get the latitude and longitude of a city using API by taking the city name as input
def get_lat_long(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_KEY}' # url to get the latitude and longitude of a city
    try:
        response = requests.get(url)   # sending a request to the url
        if response.status_code == 200:
            data = response.json() # converting the response to json format
            if data:
                return data[0]
            else:
                return None
        else:
            print("Unable to fetch data")            # printing a message if the data is not fetched
            return None
    except requests.exceptions.RequestException as e:   # handling the exception if the data is not fetched due to internet connection problem
        print()
        print("Unable to fetch data. Please check your internet connection.")
        return None

#fuction to give the weather of a city using API by taking the city name as input

def get_weather(city, latitude, longitude):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric'    # url to get the weather of a city
    try:
        response = requests.get(url)      # sending a request to the url
        if response.status_code == 200:
            data = response.json()         # converting the response to json format
            return data
        else:
            print("Unable to fetch data")
            return None
    except requests.exceptions.RequestException as e:        # handling the exception if the data is not fetched due to internet connection problem
        print()
        print("Unable to fetch data. Please check your internet connection.")
        return None
    
#main fuction to get the weather of a city

def main():
    city = input('Enter the city name: ')           # taking the city name as input
    latitude=None
    longitude=None
    coord_data = get_lat_long(city)            # calling the get_lat_long() function to get the latitude and longitude of a city
    if coord_data:
        latitude = coord_data['lat']                # getting the latitude of a city
        longitude = coord_data['lon']               # getting the longitude of a city
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
    else:
        print()
        print('No data found')
    if latitude and longitude:
        data = get_weather(city, latitude, longitude)          # calling the get_weather() function to get the weather of a city
        if data:
            city = data['name']
            print(f'City: {city}')
            country = data['sys']['country']
            print(f'Country: {country}')
            temp = data['main']['temp']
            print(f'Temperature: {temp}°C')
            feels_like = data['main']['feels_like']
            print(f'Feels Like: {feels_like}°C')
            humidity = data['main']['humidity']
            print(f'Humidity: {humidity}%')
            pressure = data['main']['pressure']
            print(f'Pressure: {pressure} hpa')
            wind_speed = data['wind']['speed']
            print(f'Wind Speed: {wind_speed} m/s')
            wind_deg = data['wind']['deg']
            print(f'Wind Degree: {wind_deg}')
            description = data['weather'][0]['description']
            print(f'Description: {description}')
            icon = data['weather'][0]['icon']
            print(f'Icon: {icon}')
            print(f'Weather: {description} ({icon})')
        
#calling the main function
if __name__ == '__main__':
    #calling the main() function continuosly until the user enters 'quit'
    while True:
        main()
        print()
        choice = input('Do you want to search again? (y/n): ')           # asking the user if he/she wants to search again
        if choice == 'n':
            break
