#phoneNubers
import phonenumbers as ph
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


number = input(" Enter Phone Number:")
number = ph.parse(number)
contry = geocoder.description_for_number(number, "en")
sim_card_provider = carrier.name_for_number(number, "en")
tine_zone = timezone.time_zones_for_number(number)
print("Country:", contry)
print("Sim Card provider", sim_card_provider)
print("Time Zone:", tine_zone)