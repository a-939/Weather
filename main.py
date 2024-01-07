import json
import httplib2
import time

recent_city = ''
auto_refresh_count = 0


# This the backend code where we fetch the weather details from server
def err_in_response(status):
    if status == 400 or status == 500:
        print("Server error, please try after some time.")
    elif status == 0:
        print("Please select valid option")
    elif status == 1006:
        print("Please valid city name")


# you can use this below free weather api
# https://api.openweathermap.org/data/2.5/weather?appid=2700cb77f169014b47963479d60e46c1
def get_weather(city):
    global recent_city
    # url = 'https://api.openweathermap.org/data/2.5/weather?' # this is openweatherapi free of cost
    url = 'https://api.weatherapi.com/v1/current.json?'  # valid for 10 days
    # appid = 2700cb77f169014b47963479d60e46c1 # this is for openweatherapi
    apikey = '84196dcb99134d34baf163255240501'
    # params = 'appid=' + appid + '&q=' + city
    params = '&key=' + apikey + '&q=' + city
    h = httplib2.Http('.cache')
    response, content = h.request(url + params)
    # print(url + params)
    # print(response.status)
    if response.status == 200:
        recent_city = city
        return get_weather_data(content)
    else:
        return err_in_response(response.status)


# This method to get the import values from the response
def get_weather_data(response):
    data = json.loads(response)
    print()
    print(data['location']['name'], data['location']['region'], data['location']['country'], sep=',')
    print(data['current']['condition']['text'])
    print()
    auto_refresh()


def auto_refresh():
    global auto_refresh_count
    if auto_refresh_count < 1:
        auto_refresh_count += 1
        time.sleep(15)
        get_weather(recent_city)
    else:
        auto_refresh_count = 0


# This is UI main method called after start the execution
def front_end():
    cities_list = ['Nancy', 'San Francisco',
                   'Nandyal', 'Kurnool', 'kadapa']
    while True:
        user_input = ''
        print()
        while True:
            print()
            print('Welcome to the weather checking Console application Dev kiru')
            print('Please select:')
            print('1. Type city name')
            print('2. Select city name in favorite city list')
            user_selection = input()
            if user_selection == '1' or user_selection == '2':
                user_input = user_selection
                break
            else:
                err_in_response(0)
        if user_input == '1':
            city = input('Enter city name: ')
            get_weather(city)
        elif user_input == '2':
            print('Please select city name in favorite city list below')
            print('Favorite city List : ')
            print(*enumerate(cities_list))
            city_number = int(input('Enter city number: '))
            get_weather(cities_list[city_number])

        if recent_city == '' or recent_city not in cities_list:
            cities_list.append(recent_city)


# It starts the main execution
if __name__ == '__main__':
    front_end()
    if recent_city != '':
        auto_refresh()
