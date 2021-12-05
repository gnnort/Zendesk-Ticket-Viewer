# Zendesk Ticket Viewer
A command-line interface application for viewing tickets on Zendesk, written in Python. The app makes HTTP requests to the Zendesk ticket API to retrieve account tickets and individual ticket details.

## Prerequisite Installations
- Python 3.7 or greater
- [Click Python library](https://click.palletsprojects.com/en/8.0.x/quickstart/#)
- [Requests Python library](https://docs.python-requests.org/en/latest/user/install/)

## Installation (Windows/MacOS)

1. Download the repository to your local machine with the following code.

```
git clone https://github.com/gnnort/Zendesk-Ticket-Viewer
```

2. Navigate to the main repository directory in your MacOS Terminal or equivalent command line application.
3. Install click and requests modules with:

```
pip install requests
pip install click 
```
## How to Use
_NOTE: The default user details will be for my account.
If you want to try this on your account, please fill in your details in Zendesk-Ticket-Viewer/authentication/user_details.txt (The redirect URI should **ALWAYS** be http://localhost:8080)_

Run the program with:
```
python main.py 
```
NOTE: You can run the individual commands with:

```
python main.py <command>
e.g. If I want to view all tickets, type 'python main.py all-tickets'
```
#### User commands
```
python main.py all-tickets
```
```
python main.py ticket-detail
```

### Running Tests

1. Navigate to the repository directory 'main_test.py' in your MacOS Terminal or equivalent command line application.
2. Run the tests with the following code

```
python main_test.py
```

### Files
- ```main.py``` : Program entry point, communicates data between components. RUN THIS
- ```commands.all_tickets.py``` : Makes request to the API to retrieve all tickets in account. Sent in chunks of 25 tickets per page
- ```commands.ticket_detail.py``` : Makes request to the API to retrieve a single ticket in account. User must specify ticket ID
- ```httphandler.py``` : Initializes server when user wants to authenticate. Server retrieves access code from Zendesk
- ```oauth.py``` : Contains functions to authenticate user
- ```main_test.py``` : Unit tests to test functionality of app



### Design Choices

#### Why Click?
Click is a Python package for creating command line interfaces and makes use of python decorators for high configurability. I chose to use click for its simplicity and speed.
For exception handling, click internally runs in standalone mode and uses exceptions to signal various error conditions that the user of the application might have caused. This has the side-effect of having an implicit sys.exit() i.e. the program exits every time a command is executed. This is fine for the purposes of my application as no values are reused. 
However, should you want to disable the implicit sys.exit(), [Click 3.0 allows you to use the Command.main() method to disable standalone mode](https://click.palletsprojects.com/en/8.0.x/exceptions/#what-if-i-don-t-want-that). NOTE: This disables exception handling.


#### Python Requests for making HTTP requests to the Zendesk API
Ticket requests make use of the python requests module, a simple and human-friendly library that supports HTTP requests. It allows you to send HTTP/1.1 requests extremely easily with no need to manually add query strings to your URLs, or to form-encode your POST data.

#### Authentication method
I implemented Oauth 2.0 via the authorization code grant flow for 2 reasons:
1. Username and Password will not be stored in the code, which would have been a security vulnerability
2. Scope limits can be defined. I have set it to _read only_

For those who would rather email and password authentication, there is a branch of the application that supports it named 'normalauth'.

#### Commands
 'all-tickets'
This command requests for the user's tickets from the Zendesk API, in chunks of 25. The code appends these 25 tickets to a list and prints out its contents to the command-line with a page number; this will continue until reaching the last page. [Cursor pagination was used for this as it is preferred over offset pagination](https://developer.zendesk.com/documentation/developer-tools/working-with-data/understanding-the-limitations-of-offset-pagination/).

 'ticket-detail'
This command takes in user input of a ticket ID (positive integer) to request for a specific ticket. Ticket IDs can be viewed using the all-tickets command.


### Resources

These are the resources that helped me along the way

- Documentation links

  - [Tickets](https://developer.zendesk.com/rest_api/docs/support/tickets#show-ticket)

  - [Basic Authentication](https://developer.zendesk.com/rest_api/docs/support/introduction#basic-authentication)

  - [Pagination](https://developer.zendesk.com/rest_api/docs/support/introduction#pagination)
  
  - [OAuth 2.0](https://support.zendesk.com/hc/en-us/articles/203663836-Using-OAuth-authentication-with-your-application)

  - [Click Documentation](https://click.palletsprojects.com/en/8.0.x/)

- Unit testing in Python

  - [Python Unit testing guide](https://docs.python-guide.org/writing/tests)

  - [How to use unittest.mock.patch to mock return values](https://www.youtube.com/watch?v=WFRljVPHrkE&t=182s)

##### Thank you to Zendesk for this fun project!😋
