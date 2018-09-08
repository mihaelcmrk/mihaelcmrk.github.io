import requests
r1 = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=YD77K7UNTCY8YQ8A')
r2 = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=6ZC0ZBT7NORMWK26')
print(r1.text,r2.text)
