# Phone-Info-Extractor
This Python script allows you to input phone numbers and get detailed information about each number, such as its location, carrier, and associated timezones.

Features
Validates Phone Numbers: Ensures the phone number is correct.
Location Information: Identifies the country or region of the phone number.
Carrier Information: Shows the network provider of the phone number.
Timezone Information: Displays the timezones related to the phone number.
How to Use
Requirements
Python 3.x
phonenumbers library (Install with pip install phonenumbers)
Steps to Run
Clone or download the script.
Run the script:
bash
Copy code
python phone_number_details_processor.py
Enter the phone numbers in the format +<country_code><number>. Example: +9178699859850.
Type done when finished to see the details.
Example Output
typescript
Copy code
Enter a phone number like this[+9178699859850] (or type 'done' to finish): +918878586271
Enter a phone number like this[+9178699859850] (or type 'done' to finish): +12136574429
Enter a phone number like this[+9178699859850] (or type 'done' to finish): done

Phone Numbers Details


Phone Number: +918878586271
Location: India
Carrier: Vodafone
Timezone: ('Asia/Calcutta',)

Phone Number: +12136574429
Location: Los Angeles, CA
Carrier: 
Timezone: ('America/Los_Angeles',)
City: Los Angeles

License
This project is licensed under the MIT License.
