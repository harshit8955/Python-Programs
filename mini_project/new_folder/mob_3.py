import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests

def get_full_details(number):
    try:
        phone = phonenumbers.parse(number)

        print("\n📱 MOBILE NUMBER DETAILS (MAX AVAILABLE)\n")

        # Basic Info
        print("Number:", number)
        print("Country Code:", phone.country_code)
        print("Region:", phonenumbers.region_code_for_number(phone))

        # Location (Approx)
        location = geocoder.description_for_number(phone, "en")
        print("Approx Location:", location)

        # Carrier
        print("Carrier:", carrier.name_for_number(phone, "en"))

        # Timezone
        print("Timezone:", ", ".join(timezone.time_zones_for_number(phone)))

        # Validity
        print("Valid:", phonenumbers.is_valid_number(phone))

        # 🌍 Extra: Get Country Info using REST API
        country_code = phonenumbers.region_code_for_number(phone)

        if country_code:
            res = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code}")
            if res.status_code == 200:
                country_data = res.json()[0]
                print("\n🌍 COUNTRY DETAILS")
                print("Country:", country_data["name"]["common"])
                print("Capital:", country_data.get("capital", ["N/A"])[0])
                print("Currency:", list(country_data.get("currencies", {}).keys()))
                print("Region:", country_data.get("region"))

    except Exception as e:
        print("❌ Error:", e)


# Run
num = input("Enter number with country code (+91...): ")
get_full_details(num)