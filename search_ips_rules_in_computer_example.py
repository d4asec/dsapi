#MY FIRST EXAMPLE FOR SEARCHING IPS RULES IN COMPUTERS
#MY FIRST EXAMPLE FOR SEARCHING IPS RULES IN COMPUTERS
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
api_instance = deepsecurity.ComputerIntrusionPreventionRuleAssignmentsRecommendationsApi(deepsecurity.ApiClient(configuration))
computer_id = 1
api_version = 'v1'
overrides = False

try:
    api_response = api_instance.list_intrusion_prevention_rule_ids_on_computer(computer_id, api_version, overrides=overrides)
    pprint(api_response)
except ApiException as e:
    print("An exception occurred when calling ComputerIntrusionPreventionRuleAssignmentsRecommendationsApi.list_intrusion_prevention_rule_ids_on_computer: %s\n" % e)

