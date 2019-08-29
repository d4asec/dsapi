#MY FIRST EXAMPLE FOR GETTING THE FULL LIST OF COMPUTERS REGISTERED IN THE DSM
from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint

# Setup
if not sys.warnoptions:
    warnings.simplefilter("ignore")
configuration = deepsecurity.Configuration()
configuration.host = 'https://192.168.75.210:4119/api'

# Authentication
configuration.api_key['api-secret-key'] = '2:PZGmBIe8rcKSF6fK2HeMkoyh5ZrC/fQeeyJyUjcpzyk='

# Initialization
# Set Any Required Values
api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(configuration))
api_version = 'v1'
overrides = False

try:
    api_response = api_instance.list_computers(api_version)
    
    for computer in api_response.computers:
        pprint(computer._host_name)
        
    #tells you the number of computers found
    num_found=len(api_response.computers)
    print("Number of computers found:" + str(num_found))
except ApiException as e:
    print("An exception occurred when calling ComputersApi.list_computers: %s\n" % e)


