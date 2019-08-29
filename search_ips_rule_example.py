#MY FIRST EXAMPLE FOR SEARCHING IPS RULES WITH AN SPECIFIC CVE
from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException

# Setup
if not sys.warnoptions:
    warnings.simplefilter("ignore")
configuration = deepsecurity.Configuration()
configuration.host = 'https://192.168.75.210:4119/api'

# Authentication
configuration.api_key['api-secret-key'] = '2:PZGmBIe8rcKSF6fK2HeMkoyh5ZrC/fQeeyJyUjcpzyk='

def getIPSrules(cve):
    # Initialization
    # Set Any Required Values
    api_instance = deepsecurity.IntrusionPreventionRulesApi(deepsecurity.ApiClient(configuration))
    api_version = 'v1'
    
    # Set search criteria for the date range
    search_criteria = deepsecurity.SearchCriteria()
    search_criteria.field_name = "CVE"
    search_criteria.string_value = "%"+cve+"%"
    
    search_filter = deepsecurity.SearchFilter(None, [search_criteria])
    
    try:
        ipsrules = api_instance.search_intrusion_prevention_rules(api_version, search_filter=search_filter)
 
        i=0
        for ipsrid in ipsrules.intrusion_prevention_rules:
            ipsruleidentifier = ipsrid.identifier
            ipsrulename = ipsrid.name
            print("ID: " + str(ipsruleidentifier),"- " + str(ipsrulename))
            i +=1
    
    except ApiException as e:
        print("An exception occurred when calling IntrusionPreventionRulesApi.search_intrusion_prevention_rules: %s\n" % e)

cvelist = [ 
"CVE-2008-0106"
           ] 
for a in cvelist:
    getIPSrules(a)

