import phonenumbers

from  phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

def tel_number_verify(Phonenumber) :
    number = phonenumbers.parse(Phonenumber)

    # the second parameter is language we want to see in UI
    country_by_telcode = geocoder.description_for_number(number,'th')
    company_mobile = carrier.name_for_number(number,'th')
    user_timezone = timezone.time_zones_for_number(number)

    return {"country" : country_by_telcode, "company_mobile" : company_mobile, "timezone" : user_timezone}



