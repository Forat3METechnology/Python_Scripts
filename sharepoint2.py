import msal
from msal import PublicClientApplication
import webbrowser #maybe we don't need it


APPLICATION_ID = "96e09680-c46e-460b-9ba4-4c3ab2a64a68" #Client ID
TENANT_ID = "8338d39d-4326-4480-8e86-7abc52095fcc"

"""
SCOPES = [
    "Files.ReadWrite.All",
    "Sites.ReadWrite.All",
    "User.Read",
    "User.ReadBasic.All"
]
"""
SCOPES = [
    "Files.ReadWrite.All",
    "Files.ReadWrite.All",
    "Sites.Read.All",
    "Sites.ReadWrite.All",
    "User.Export.All",
    "User.Read",
    "User.Read.All",
    "User.ReadBasic.All",
    "User.ReadWrite.All"

    #"ConsentRequest.Read.All",
    #"ConsentRequest.Read.All",
    #"ConsentRequest.ReadWrite.All",
    #"ConsentRequest.ReadWrite.All",
    #"DelegatedPermissionGranted.Read",

    #"Application.Read.All",
    #"Application.ReadWrite.All",
    #"Application.ReadWrite.All"
]

#3me tenant url
#authority_url = "https://login.microsoftonline.com/consumers" #url we need to use to login to access the access_token
#authority_url = "https://login.microsoftonline.com/common/adminconsent?client_id=your_client_id"
authority_url = "https://login.microsoftonline.com/"+TENANT_ID

base_url = "https://graph.microsoft.com/v1.0/"
endpoint = base_url + "me" #me is the service name that we would like to access

#login to acquire access_token
app = PublicClientApplication(
    APPLICATION_ID,
    authority=authority_url
)

"""
accounts = app.get_accounts()#get the accounts to sign in onto Microsoft from the cache
if accounts:#if there are accounts in cache
    app.acquire_token_silent(scopes=SCOPES,account=accounts[0])
"""

flow = app.initiate_device_flow(scopes=SCOPES)
print(flow)
print(flow["message"])
webbrowser.open(flow["verification_uri"])

#aquire app token
result = app.acquire_token_by_device_flow(flow)

if "access_token" in result:
    print(result)
else:
    raise Exception("No access token")

#print(result)
