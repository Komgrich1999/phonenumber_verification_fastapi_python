from fastapi import FastAPI
from datetime import date
import phonenumbers

from  phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

from phonenumber_verify import tel_number_verify

app = FastAPI()

@app.get("/")
def index() :
    return {"message" : f"Hello Fast API {date.today()}"}

@app.get("/{phone_number}")
def phone_number(phone_number : str):
    return tel_number_verify(phone_number)

