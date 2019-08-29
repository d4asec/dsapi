#MY FIRST EXAMPLE FOR ASSIGNING POLICIES TO COMPUTERS
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
api_instance = deepsecurity.PoliciesApi(deepsecurity.ApiClient(configuration))
api_version = 'v1'

search_criteria = deepsecurity.SearchCriteria()
search_criteria.field_name = "name"
search_criteria.string_test = "equal"
search_criteria.string_value = "%Linux Server%"

# Create a search filter
search_filter = deepsecurity.SearchFilter(None, [search_criteria])
policies_api = deepsecurity.PoliciesApi(deepsecurity.ApiClient(configuration))
computers_api = deepsecurity.ComputersApi(deepsecurity.ApiClient(configuration))
computer = deepsecurity.Computer()

try:
    # Perform the search
    policy_search_results = policies_api.search_policies(api_version, search_filter=search_filter)

    # Assign the policy to the computer
    computer.policy_id = REPLACE_WITH_THE_POLICY_ID_TO_ASSIGN

    computers_api.modify_computer(REPLACE_WITH_THE_COMPUTER_ID_TO_MODIFY, computer, api_version)

except ApiException as e:
    pprint( "Exception: " + str(e))

