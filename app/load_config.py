import json


with open("config.json", mode="r") as cfg:
    data = json.loads(cfg.read())

    Y_MUSIC_KEY = data.get("y_music_api_key")
    CLIENT_ID = data.get("presence_client_id")
