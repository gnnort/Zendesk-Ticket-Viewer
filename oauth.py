from requests.api import head
from httphandler import run_server
from urllib.parse import urlencode
import os.path
import requests
import json
import webbrowser



def get_initial_code():
    parameters = {
            'response_type': 'code',
            'redirect_uri': 'http://localhost:8080',
            'client_id': 'tron_zendesk_ticket_viewer',
            'scope': 'read'}
    url = 'https://tron7825.zendesk.com/oauth/authorizations/new?' + urlencode(parameters)
    webbrowser.open(url, new = 1, autoraise= True)                                             #webbrowser must be opened first before running server. new = 1 opens in new browser window if possible
    retrieved_code = run_server()
    if retrieved_code == "Error":
        print("Authentication Failed when attempting to retrieve initial code from API")                                                              #spin up server to listen for get request and retrieve code
    return retrieved_code


def get_access_token(retrieved_code):
    parameters = {
            'grant_type': 'authorization_code',
            'code': retrieved_code,
            'client_id': 'tron_zendesk_ticket_viewer',
            'client_secret': '0dc2350f7a5b8242b87f62bd72869f4cceff618850212a7c8146d86c2028840c',
            'redirect_uri': 'http://localhost:8080',
            'scope': 'read write'}
    payload = json.dumps(parameters)
    header = {'Content-Type': 'application/json'}
    url = 'https://tron7825.zendesk.com/oauth/tokens'
    r = requests.post(url, data=payload, headers=header)
    if r.status_code != 200:
        print("Could not receive access token from API")
        return 'Failed'
    else:
        data = r.json()
        access_token = data['access_token']
        return access_token


def authenticate(): #returns a boolean value
    
    my_code = get_initial_code()
    if my_code == "Error":
        return False

    my_access_token = get_access_token(my_code)
    if my_access_token == 'Failed':
        return False

    final_access_token = my_access_token
    bearer_token = 'Bearer ' + final_access_token
    header = {'Authorization': bearer_token}

    with open('oauth_token.json', 'w') as oauthFile:
        json.dump(header, oauthFile)
    return True

def retrievedOauthtoken():  #returns a boolean value True or False
    boolean = os.path.isfile("oauth_token.json")
    return boolean



def main():
    pass

if __name__ == "__main__":
    main()