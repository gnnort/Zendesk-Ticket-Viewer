def make_request():
    has_token = False
    if has_token:
        #start get request
        pass
    else:
        #start auth flow
        pass

def handle_decision(CODE):
    if CODE == "Error":
        return "Authentication Failed"
    else: #get access token
        parameters = {
            'grant_type': 'authorization_code',
            'code': CODE,
            'client_id': 'oauth_tutorial_app',
            'client_secret': '{your_secret}',
            'redirect_uri': 'http://localhost:8080/handle_user_decision',
            'scope': 'read'}
        payload = json.dumps(parameters)
        header = {'Content-Type': 'application/json'}
        url = 'https://tron7825.zendesk.com/oauth/tokens'
        r = requests.post(url, data=payload, headers=header)
        if r.status_code != 200:
            error_msg = 'Failed to get access token with error {}'.format(r.status_code)
            return template('error', error_msg=error_msg)
        else:
            data = r.json()
            token = data['access_token']