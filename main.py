import json
import os
import pprint

from fastapi import FastAPI

app  = FastAPI()

def _log(message):
    pprint.pprint(message)

@app.get("/")
def phones():
    res = []
    cwd = os.getcwd()
    dir_list = os.listdir(cwd+"/phones")
    
    _log(dir_list)
    
    for file_name in dir_list:
        _log(file_name)
        f = open("phones/"+file_name)
        data = json.load(f)
        res.append(data)
    
    return res

