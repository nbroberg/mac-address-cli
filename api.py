import re
import requests
import urllib.parse
import logging
import json

API_URL = 'https://api.macaddress.io/v1?'


class MacAddressAPI:
    __api_key: str
    __log_level: str

    def __init__(self, api_key, log_level):
        if not MacAddressAPI.__validate_api_key(api_key):
            raise ValueError('API Key improperly formatted')

        self.__api_key = api_key
        self.__log_level = log_level

    # For security, we don't want anything other than valid keys getting passed to API
    def __validate_api_key(api_key):
        return (re.match("^[A-z_]{32}$", api_key))

    # For security, we don't want anything other than valid MAC addresses getting passed to API
    def __validate_mac_address(mac_address):
        return (re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()))

    def __request(self, mac_address):
        api_params = {
            'apiKey': self.__api_key,
            'search': mac_address.replace(':', ''),
            'output': 'json'
        }
        request_url = API_URL + urllib.parse.urlencode(api_params)
        response = requests.get(request_url)
        return response.json()

    # Handles error and normal runtime output
    def __format_output(self, mac_address, company='', error=None):
        # Defaults to JSON output unless log level set below CRITICAL
        json_only = (self.__log_level == 'CRITICAL')

        output = {}
        output['MAC Address'] = mac_address
        if error:
            error_string = str(error)
            logging.error(error_string)
            output['Error'] = error_string
        elif company == '' or company == None:
            logging.warn(f"No company name found for {mac_address}")
            output['Company Name'] = None
        else:
            logging.info(f"Company name '{company}' found for {mac_address}!")
            output['Company Name'] = company

        if json_only:
            return json.dumps(output)
        else:
            return ''

    # Only API Call Available: get company name from MAC address
    def get_company_name(self, mac_address):
        if not MacAddressAPI.__validate_mac_address(mac_address):
            return self.__format_output(mac_address, error='Invalid MAC address')

        try:
            response = self.__request(mac_address)
            if 'error' in response.keys() and response['error']:
                raise requests.exceptions.RequestException(response['error'])
        except requests.exceptions.RequestException as e:
            return self.__format_output(mac_address, error=e)

        company = response.get('vendorDetails', {}).get('companyName')
        return self.__format_output(mac_address, company=company)
