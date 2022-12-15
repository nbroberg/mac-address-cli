from api import MacAddressAPI
import argparse
import os
import logging

# Allows environment variable to be used as default in argparse or sets required True
def env_or_required(key):
    return (
        {'default': os.environ.get(key)} if os.environ.get(key)
        else {'required': True}
    )


# Starts CLI if this file is run directly
if __name__ == "__main__":
    # Allows setting command line parameters
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--api-key', **env_or_required('API_KEY'))
    argparser.add_argument('--mac-address', required=True)
    argparser.add_argument('--log-level', default='CRITICAL')
    args = argparser.parse_args()

    # Set log level based on CLI args
    logging.basicConfig(
        format='%(asctime)s %(levelname)-5s %(message)s',
        level=args.log_level
    )

    # Requests data from api.macaddress.io
    mac_address_api = MacAddressAPI(args.api_key, args.log_level)
    json_response = mac_address_api.get_company_name(args.mac_address)
    print(json_response)
