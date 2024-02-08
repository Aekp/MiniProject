# hue_controller.py
import requests
import json

# Philips Hue API credentials
bridge_ip = '192.168.1.69'  # Replace with your bridge IP
username = '8yItBsfeLN0ehCZaY2ci5E3FjlrPT9BEOrJU74zG'  # Replace with your Hue API username

# Base URL for the Philips Hue API
base_url = f'http://{bridge_ip}/api/{username}'

# Function to set light color and brightness
def set_light_color_and_brightness(light_id, x, y, brightness):
    """
    Set the color and brightness of a specific light.
    """
    url = f'{base_url}/lights/{light_id}/state'
    payload = {
        "on": True,
        "xy": [x, y],
        "bri": brightness
    }
    response = requests.put(url, json=payload)
  

# Function to turn off a specific light
def turn_off_light(light_id):
    """
    Turn off a specific light.
    """
    url = f'{base_url}/lights/{light_id}/state'
    payload = {"on": False}
    response = requests.put(url, json=payload)
    

# Function to turn on a specific light
def turn_on_light(light_id):
    """
    Turn on a specific light.
    """
    url = f'{base_url}/lights/{light_id}/state'
    payload = {"on": True}
    response = requests.put(url, json=payload)
    

def turn_on_all_lights():
    """
    Turn on all lights registered with the Philips Hue Bridge.
    """
    response = requests.get(f'{base_url}/lights')
    if response.ok:
        lights = response.json()
        for light_id in lights:
            turn_on_light(light_id)
        print("All lights have been turned on.")
    else:
        print("Failed to retrieve light information.")

def set_all_lights_color_and_brightness(x, y, brightness):
    """
    Set the color and brightness for all lights registered with the Philips Hue Bridge.
    """
    response = requests.get(f'{base_url}/lights')
    if response.ok:
        lights = response.json()
        for light_id in lights:
            set_light_color_and_brightness(light_id, x, y, brightness)
        

# Debug print to check if the script can connect to the bridge
try:
    response = requests.get(f'{base_url}/lights')
    if response.ok:
        print("Successfully connected to the Philips Hue Bridge.")
    else:
        print("Failed to connect to the Philips Hue Bridge.")
except requests.exceptions.RequestException as e:
    print(f"Error connecting to the Philips Hue Bridge: {e}")

# Call the function to turn on all lights
#turn_on_all_lights()