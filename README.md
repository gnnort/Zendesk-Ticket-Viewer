# Zendesk Ticket Viewer
A command-line interface application for viewing tickets on Zendesk, written in Python. The app makes HTTP requests to the Zendesk ticket API to retrieve account tickets and individual ticket details.

## Prerequisite Installations
- Python 3.7 or greater
- [Click Python library](https://click.palletsprojects.com/en/8.0.x/quickstart/#) (installing in virtual environment recommended)
- [Requests Python library](https://docs.python-requests.org/en/latest/user/install/)

## How to run (MacOS/Windows)

1. Download the repository to your local machine with the following code.

```
$ git clone https://github.com/gnnort/Zendesk-Ticket-Viewer
```

2. Navigate to the main repository directory in your MacOS Terminal or equivalent command line application.
3. Install click and requests modules with the following code

```
$ pip install requests
$ pip install click #install to virtual env?
```

4. Run the program with the following code.

```
$ python main.py 
```
#### Running Tests

1. Navigate to the repository directory 'main_test.py' in your MacOS Terminal or equivalent command line application.
2. Run the tests with the following code

```
$ python main_test.py
```
## Learning Resources
- [Click Documentation](https://click.palletsprojects.com/en/8.0.x/)
- [Unittest Guide](link)

### User commands
```
python main.py all-tickets
```
```
python main.py ticket-detail
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
The main version of the ticket viewer uses Oauth 2.0 for authentication via the authorization code grant flow. This is for added security as the user's email and password are never stored in the code. The scope of access can also be configured. (It is set to read-only for this application)
For those who would rather email and password authentication, there is a branch of the application that supports it.


### Commands

#### 'all-tickets'
This command requests for the user's tickets from the Zendesk API, in chunks of 25. The code appends these 25 tickets to a list and prints out its contents to the command-line with a page number; this will continue until reaching the last page. [Cursor pagination was used for this as it is preferred over offset pagination](https://developer.zendesk.com/documentation/developer-tools/working-with-data/understanding-the-limitations-of-offset-pagination/).

#### 'ticket-detail'
This command takes in user input of a ticket ID (positive integer) to request for a specific ticket. Ticket IDs can be viewed using the all-tickets command.


### Resources
-Zendesk documentation links
    - [OAuth 2.0](https://support.zendesk.com/hc/en-us/articles/203663836-Using-OAuth-authentication-with-your-application)
    - [Tickets](https://developer.zendesk.com/rest_api/docs/support/tickets#show-ticket)
    - [Pagination](https://developer.zendesk.com/rest_api/docs/support/introduction#pagination)

-Unit Testing links
    - [Python Unit testing guide](https://docs.python-guide.org/writing/tests)
    - [How to use unittest.mock.patch to mock return values](https://www.youtube.com/watch?v=WFRljVPHrkE&t=182s)
