import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# 📞 Enter phone number with country code
number = input("Enter phone number with country code (e.g. +919876543210): ")

# 🔍 Parse number
phone_number = phonenumbers.parse(number)

# ✅ Check validity
is_valid = phonenumbers.is_valid_number(phone_number)

# 🌍 Get details
country = geocoder.description_for_number(phone_number, "en")
sim_carrier = carrier.name_for_number(phone_number, "en")
time_zones = timezone.time_zones_for_number(phone_number)

# 📊 Output
print("\n📱 PHONE NUMBER DETAILS\n")
print("Number:", number)
print("Valid:", is_valid)
print("Country/Location:", country)
print("Carrier:", sim_carrier)
print("Time Zones:", ", ".join(time_zones))