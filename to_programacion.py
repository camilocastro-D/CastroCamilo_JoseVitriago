from consumo_api import get_weather_city

print ("app del clima mundial")
#user = int(input("ingrese A si quiere que la busqueda sea por nombre de la ciudad o ingrese B si quiere que la busqueda sea por longitud y latitud"))


params ={}
params ["q"] = "London"
params  ["appid"] = "a819530cf94d3ae1253831c55d4217af"

url = "https://api.openweathermap.org/data/2.5/weather" 
clima = get_weather_city(url,params)

print (clima["main"])




   