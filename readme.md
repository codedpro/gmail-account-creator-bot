# Gmail Bot

This project automates the process of creating Gmail accounts using Selenium WebDriver and Faker for generating random user data. It also includes a script to obtain temporary phone numbers and retrieve SMS codes for phone verification.

## Features

- **Automated Gmail Signup:** Fills out the Gmail signup form with random user details.
- **Phone Number Integration:** Uses the SMS-Activate API to get temporary phone numbers and retrieve SMS codes.
- **Random Data Generation:** Utilizes the Faker library to generate realistic names and passwords.
- **Cross-browser Support:** Example scripts for Safari and Edge browsers.

## Files

- `main.py`: Automates Gmail signup using Safari and Faker.
- `test.py`: Alternative Gmail signup automation using Edge, with improved error handling and retry logic.
- `get-sms.py`: Fetches temporary phone numbers and retrieves SMS codes from the SMS-Activate API.

## Requirements

- Python 3.7+
- Selenium
- Faker
- requests
- Edge or Safari WebDriver (depending on the script)

## Installation

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install selenium faker requests
   ```
3. Download and set up the appropriate WebDriver for your browser (Safari or Edge).

## Usage

### 1. Gmail Signup Automation

Run the main script:

```bash
python main.py
```

Or run the alternative script:

```bash
python test.py
```

### 2. Get Temporary Phone Number and SMS

```bash
python get-sms.py
```

## Notes

- The SMS-Activate API key is hardcoded in `get-sms.py`. Replace it with your own for production use.
- Automating Gmail signup may violate Google's terms of service. Use responsibly and for educational purposes only.

## License

This project is for educational purposes only.
