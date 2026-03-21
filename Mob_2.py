import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type

def get_phone_details(number):

    try:
        # Parse number
        phone = phonenumbers.parse(number)

        print("\n📱 MOBILE NUMBER FULL DETAILS\n")

        # 📌 Basic Info
        print("Input Number:", number)
        print("International Format:", phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
        print("National Format:", phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.NATIONAL))
        print("E164 Format:", phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164))

        # 🌍 Region Info
        print("Country Code:", phone.country_code)
        print("Region Code:", phonenumbers.region_code_for_number(phone))

        # ✅ Validity
        print("Valid Number:", phonenumbers.is_valid_number(phone))
        print("Possible Number:", phonenumbers.is_possible_number(phone))

        # 📡 Carrier
        print("Carrier:", carrier.name_for_number(phone, "en"))

        # 📍 Location
        print("Location:", geocoder.description_for_number(phone, "en"))

        # ⏰ Timezone
        print("Timezone:", ", ".join(timezone.time_zones_for_number(phone)))

        # 📶 Number Type
        num_type = number_type(phone)
        type_dict = {
            0: "Fixed Line",
            1: "Mobile",
            2: "Fixed Line or Mobile",
            3: "Toll Free",
            4: "Premium Rate",
            5: "Shared Cost",
            6: "VoIP",
            7: "Personal Number",
            8: "Pager",
            9: "UAN",
            10: "Voicemail",
            -1: "Unknown"
        }
        print("Number Type:", type_dict.get(num_type, "Unknown"))

    except Exception as e:
        print("❌ Error:", str(e))


# ▶ Run
number = input("Enter mobile number with country code (+91...): ")
get_phone_details(number)