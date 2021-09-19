import requests
import json

def make_request_to_api():
    
    
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":"Christchurch","days":"3"} #CHANGE QUERY STRING FOR CURRENT CITY 

    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "12345679" #ADD YOUR RAPID API KEY HERE FOT WEATHERAPI
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    return json.loads(response.text)


def process_request(json_data):
    
    return_str = ''

    forecast = json_data['forecast']
    forecast_day = forecast["forecastday"][0]
    hours = forecast_day['hour']
    
    headwind = False
    tailwind = False
    rainlst = {}
    speedlst = {}

    for hour in hours[15:18]: #24hr time, alter for different time
        if hour['precip_mm'] != 0:
            rainlst[hour['time']] = hour['precip_mm']

        if hour['wind_degree'] in range(80, 120+1) and (hour['wind_kph'] > 10 or hour['gust_kph'] > 25):
            
            headwind = True
            speedlst[hour['time']] = hour['wind_kph']
            
        elif (hour['wind_degree'] in range(250, 291)):
            tailwind = True
            speedlst[hour['time']] = hour['wind_kph']


    if headwind:
        temp = min(speedlst.values())
        vari = [key for key in speedlst if speedlst[key] == temp]
        res = (vari[0]).split(" ")[1]
        return_str = f"{res} is the lowest headwind of {temp}km/h."
        
        if vari[0] in list(rainlst.keys()):
            return_str += f"\nExpected precip of {hour['precip_mm']}mm"
        else:
            return_str += "\nNo precip expected"

    elif tailwind:
        temp = max(speedlst.values())
        vari = [key for key in speedlst if speedlst[key] == temp]
        res = (vari).split(" ")[1]
        return_str = f"{res} is the best tailwind of {temp}km/h."
        
        if vari[0] in list(rainlst.keys()):
            return_str += f"\nExpected precip of {hour['precip_mm']}mm"
        else:
            return_str += "\nNo precip expected"

    return return_str

def main_func():
    response = make_request_to_api()
    message_to_send = process_request(response)

    return message_to_send



if __name__ == "__main__":

    main_func()
