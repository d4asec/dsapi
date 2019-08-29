#MY FIRST EXAMPLE FOR SEARCHING COMPUTERS WITH CRITERIA
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

search_criteria = deepsecurity.SearchCriteria()
search_criteria.field_name = "hostName"
search_criteria.string_test = "equal"
search_criteria.string_value = "%192.168.%"

search_filter = deepsecurity.SearchFilter(None, [search_criteria])
overrides = False

try:
    api_response = api_instance.search_computers(api_version, search_filter=search_filter, overrides=overrides)
    pprint(api_response)
except ApiException as e:
    print("An exception occurred when calling ComputersApi.search_computers: %s\n" % e)


