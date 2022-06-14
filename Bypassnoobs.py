import threading
import requests
import json
import time


print("Nicedayz Bypass log Huhhh")


token = ""  # input("TOKEN > ")
Guild_ID = input("Guild ID > ")



def Nicedayz():
    global Guild_ID
    while True:
        try:
            r = requests.patch(f"https://discord.com/api/v9/guilds/{Guild_ID}", headers={"Authorization": F"{token}"}, json={"features": ["COMMUNITY"], "preferred_locale": "en-US", "rules_channel_id": "1", "public_updates_channel_id": "1"})
            s = [200, 201, 204]
            if r.status_code in s:
                print("Yaaahoooooo")
            elif r.status_code == 429:
                b = r.json()
                time.sleep(b['retry_after'])
        except:
            pass
        try:
            r = requests.patch(f"https://discord.com/api/v9/guilds/{Guild_ID}", headers={"Authorization": F"{token}"}, json={"description": None, "features": ["NEWS"], "preferred_locale": "en-US", "rules_channel_id": None, "public_updates_channel_id": None})
            s = [200, 201, 204]
            if r.status_code in s:
                print("YaaahooooooRetry")
            elif r.status_code == 429:
                b = r.json()
                time.sleep(b['retry_after'])
        except:
            pass

def Nicedayz1():
    for i in range(1000):
        t = threading.Thread(target=Nicedayz)
        t.start()
Nicedayz1()
