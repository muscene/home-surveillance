import requests
import socket

# Function to get the public IP address
def get_public_ip():
    try:
        # Use a web service to get the public IP address
        response = requests.get('https://ipinfo.io')
        
        if response.status_code == 200:
            data = response.json()
            return data.get('ip')
    except Exception as e:
        print(f"An error occurred while getting the public IP: {e}")
    
    # If the request fails, fall back to getting the local IP
    return socket.gethostbyname(socket.gethostname())

# Function to get geolocation information based on an IP address
def get_geolocation_info(ip_address):
    try:
        # Make a GET request to the "ipinfo.io" API
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and return geolocation information
            return {
                'ip': data.get('ip'),
                'city': data.get('city'),
                'region': data.get('region'),
                'country': data.get('country'),
                'loc': data.get('loc')  # Latitude and Longitude
            }
        else:
            return None  # Request was not successful
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage:
public_ip = get_public_ip()
if public_ip:
    print("Public IP Address:", public_ip)
    geolocation_info = get_geolocation_info(public_ip)
    if geolocation_info:
        print("Geolocation Information:")
        print("City:", geolocation_info['city'])
        print("Region:", geolocation_info['region'])
        print("Country:", geolocation_info['country'])
        print("Latitude and Longitude:", geolocation_info['loc'])
    else:
        print("Failed to retrieve geolocation information.")
else:
    print("Failed to retrieve the public IP address.")
