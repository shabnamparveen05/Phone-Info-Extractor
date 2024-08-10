# Phone Number Details Processor

This Python script processes and prints details for phone numbers. It uses the `phonenumbers` library to provide information such as the location, carrier, and timezone of the phone number.

## Features

- **Parse Phone Numbers**: Parses and validates phone numbers.
- **Location**: Retrieves the general location (country/region).
- **Carrier**: Identifies the network provider.
- **Timezone**: Lists the timezones associated with the phone number.
- **City Extraction**: Attempts to extract city-level information if available.

## Requirements

- Python 3.x
- `phonenumbers` library

You can install the `phonenumbers` library using pip:

```bash
pip install phonenumbers

Usage
Run the Script: Execute the script in a Python environment.
Input Phone Numbers: Enter phone numbers in the format +<country_code><number>. For example: +9178699859850.
Finish Input: Type done to stop entering phone numbers and see the results.

Example 
Enter a phone number like this[+9178699859850] (or type 'done' to finish): +14155552671
Enter a phone number like this[+9178699859850] (or type 'done' to finish): +442083661177
Enter a phone number like this[+9178699859850] (or type 'done' to finish): done

Phone Numbers Details

Phone Number: +14155552671
Location: United States
Carrier: AT&T
Timezone: ('America/New_York',)

Phone Number: +442083661177
Location: United Kingdom
Carrier: BT Group
Timezone: ('Europe/London',)

Contributing
Feel free to submit issues, improvements, or suggestions. Pull requests are welcome!
