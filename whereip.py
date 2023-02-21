import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    print(ip_address)
    #response = requests.get(f"https://ipapi.co/{ip_address}/json/")
    #response=response.json()
    #location_data = {
    #    "ip": ip_address,
    #    "city": response.get("city"),
    #    "region": response.get("region"),
    #    "country": response.get("country_name")
    #}
    #return location_data
    return "data"

print(get_location())