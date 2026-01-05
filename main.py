import base64
import json

import requests
from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def get_skin(name: str):
    name_dump = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
    id = (name_dump.json())["id"]
    skin_dump = requests.get(
        f"https://sessionserver.mojang.com/session/minecraft/profile/{id}"
    )
    encoded_skin_url = (((skin_dump.json())["properties"])[0])["value"]
    decoded_bytes = base64.b64decode(encoded_skin_url)
    skin_url = (json.loads((decoded_bytes.decode("utf-8"))))["textures"]["SKIN"]["url"]
    return skin_url
