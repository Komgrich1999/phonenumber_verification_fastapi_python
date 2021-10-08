from fastapi import FastAPI
from datetime import date
import phonenumbers

from  phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

import phonenumber_verify as pv

app = FastAPI()

@app.get("/")
def index() :
    return {"message" : f"Hello Fast API {date.today()}"}

@app.get("/{phone_number}")
def phone_number(phone_number : str):
    return pv.tel_number_verify(phone_number)

