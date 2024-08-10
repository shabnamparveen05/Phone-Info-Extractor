import phonenumbers
from phonenumbers import geocoder, carrier, timezone


# Function to process and print details of a phone number
def print_phone_number_details(phone_number_str):
    try:
        # Parsing the phone number
        phone_number = phonenumbers.parse(phone_number_str)

        # Checking if the phone number is valid
        if not phonenumbers.is_valid_number(phone_number):
            print(f"Invalid phone number: {phone_number_str}")
            return

        # Get the general location (country/region)
        location = geocoder.description_for_number(phone_number, 'en')

        # Get the carrier (network provider)
        phone_carrier = carrier.name_for_number(phone_number, 'en')

        # Get the timezones
        phone_timezone = timezone.time_zones_for_number(phone_number)

        # Display the information
        print(f"\nPhone Number: {phone_number_str}")
        print(f"Location: {location}")
        print(f"Carrier: {phone_carrier}")
        print(f"Timezone: {phone_timezone}")

        # If you want to add more detailed logic to try and get city-level data:
        if location and " " in location:
            city = location.split(",")[0]
            print(f"City: {city}")

    except phonenumbers.NumberParseException:
        print(f"Error: The phone number '{phone_number_str}' is not valid.\n")


# Prompt the user to input phone numbers
phone_numbers = []
while True:
    phone_number = input("Enter a phone number like this[+9178699859850] (or type 'done' to finish): ")
    if phone_number.lower() == 'done':
        break
    phone_numbers.append(phone_number)

# Printing a header for better readability
print('\nPhone Numbers Details\n')

# Processing each phone number
for phone_number in phone_numbers:
    print_phone_number_details(phone_number)
