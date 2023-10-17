import json
import os
import pprint

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app  = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def _log(message):
    pprint.pprint(message)

@app.get("/phones")
def phones(match: str = ""):
    res = []
    phone_list = json.load(open(os.getcwd() + "/phones.json"))
        
    if match == "":
        return  phone_list
    print(match)
    for phone in phone_list:
        print(phone["name"].casefold())

        if match.casefold() in phone["name"].casefold():            
            res.append(phone)
    return res


@app.get("/phones/{phone_id}")
def phone(phone_id: str):
    _log(phone_id)
    return json.load(open(os.getcwd() + "/phones/" + phone_id + ".json"))
    

