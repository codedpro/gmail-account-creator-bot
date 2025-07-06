import requests
import time

API_KEY = '071165868f274b1A91516791f93024b2'

def get_phone_number(service='ot', country='0'):
    url = f'https://sms-activate.org/stubs/handler_api.php?api_key={API_KEY}&action=getNumber&service={service}&country={country}'
    response = requests.get(url)
    if response.status_code == 200 and response.text.startswith('ACCESS_NUMBER'):
        _, activation_id, phone_number = response.text.split(':')
        return activation_id, phone_number
    else:
        raise Exception(f"Failed to get phone number: {response.text}")

def get_sms(activation_id):
    url = f'https://sms-activate.org/stubs/handler_api.php?api_key={API_KEY}&action=getStatus&id={activation_id}'
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            if response.text.startswith('STATUS_OK'):
                _, sms = response.text.split(':')
                return sms
            elif response.text == 'STATUS_WAIT_CODE':
                print("Waiting for SMS...")
                time.sleep(10)
            else:
                raise Exception(f"Failed to get SMS: {response.text}")
        else:
            raise Exception(f"Error: {response.status_code}")

def main():
    try:
        activation_id, phone_number = get_phone_number()
        print(f"Phone Number: {phone_number}")
        print(f"Activation ID: {activation_id}")

        sms = get_sms(activation_id)
        print(f"Received SMS: {sms}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
