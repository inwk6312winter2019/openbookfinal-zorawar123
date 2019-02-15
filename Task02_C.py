from requests import get

ip = get('https:/api.org").text
print(" IP is:", ip)
