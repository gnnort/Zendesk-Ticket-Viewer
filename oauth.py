from httphandler import get_code, run_server
from urllib.parse import urlencode
import requests
import json

def get_initial_code():
    run_server()
    parameters = {
            'response_type': 'code',
            'redirect_uri': 'http://localhost:8080',
            'client_id': 'tron_zendesk_ticket_viewer',
            'scope': 'read'}
    url = 'https://tron7825.zendesk.com/oauth/authorizations/new?' + urlencode(parameters)
    print(url)
    return get_code()

def get_access_token():
    parameters = {
            'grant_type': 'authorization_code',
            'code': get_initial_code(),
            'client_id': 'tron_zendesk_ticket_viewer',
            'client_secret': 'bee44a1a253509adbd787f92d95d4bf4fb95ddd2e9e498f05d6216e9449ddcb6 ',
            'redirect_uri': 'http://localhost:8080',
            'scope': 'read'}
    payload = json.dumps(parameters)
    header = {'Content-Type': 'application/json'}
    url = 'https://your_subdomain.zendesk.com/oauth/tokens'
    r = requests.post(url, data=payload, headers=header)
    if r.status_code != 200:
        print("couldnt get access token")
    else:
        data = r.json()
        access_token = data['access_token']
        return access_token

def authenticate():
    access_token = get_access_token()
    bearer_token = 'Bearer ' + access_token
    header = {'Authorization': bearer_token}