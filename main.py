import json
import httplib2


# This the backend code where we fetch the weather details from server
def err_in_response():
    return "Server error, please try after some time."


def get_weather(city):
    url = 'https://api.weatherapi.com/v1/current.json?'
    apikey = '84196dcb99134d34baf163255240501'
    params = '&key=' + apikey + '&q='+city
    h = httplib2.Http('.cache')
    response, content = h.request(url+params)
    if response.status == 200:
        return get_weather_data(content)
    else: 
        return err_in_response()


# This method to get the import values from the response
def get_weather_data(response):
    data = json.loads(response)
    # TODO: Here You can print what ever details you want from the response
    print(data['location']['name'])
    # TO check the structure print data and check in the console


# TODO: create this method automatic refresh every 15-30 sec
def auto_refresh():
    pass


# TODO: create the UI
# This is UI main method called after start the execution
def front_end():
    print()


# It starts the main execution
if __name__ == '__main__':
    get_weather("nandyal")
