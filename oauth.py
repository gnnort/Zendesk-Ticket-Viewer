from requests.api import head
from httphandler import run_server
from urllib.parse import urlencode
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
    webbrowser.open(url, new = 1, autoraise= False)
    print(url)
    retrieved_code = run_server()
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
        print(r.reason)
        return 'paddington'
    else:
        data = r.json()
        access_token = data['access_token']
        return access_token


def authenticate():
    my_code = get_initial_code()
    my_access_token = get_access_token(my_code)
    if my_access_token == 'paddington':
        return "Unable to get final accesstoken"
    final_access_token = my_access_token
    bearer_token = 'Bearer ' + final_access_token
    header = {'Authorization': bearer_token}
    return header





def main():
    pass

if __name__ == "__main__":
    main()