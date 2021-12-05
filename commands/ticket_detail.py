import sys
import click
import requests
import calendar
import json
from datetime import datetime
from authentication.oauth import authenticate, retrievedOauthtoken

with open('authentication/user_details.json') as user_details_file:
    user_details = json.load(user_details_file)
    subdomain = user_details['subdomain']



@click.group()
def ticket_detail_group():
    pass


@ticket_detail_group.command()
@click.pass_context
def ticket_detail(context):
    if retrievedOauthtoken():
        with open('authentication/oauth_token.json') as json_header_file:                                                          #reads local json file for header
            header_data = json.load(json_header_file)
        goodinput = False
        while goodinput == False:
            id = click.prompt('Please enter a valid Ticket ID')
            url = "https://{subdomain}.zendesk.com/api/v2/tickets/" + str(id) + ".json"

            try:
                id = int(id)
            except ValueError:
                click.echo("Please ensure your input is a positive integer. Try Again!")
                continue

            if id <= 0:
                click.echo("Please ensure your input is a positive integer. Try Again!")

            else:
                goodinput = True    #break out of while loop
                try:
                    response = requests.get(url, headers = header_data, timeout=10)

                    if response.status_code >= 500:
                            click.echo(f'Status: {response.status_code} API is unavailable.\n\tExiting...')
                    elif response.status_code == 404:
                            click.echo(f'Status: 404 ticket not found. Ensure the ticket id exists!')
                    elif response.status_code >= 400:
                            click.echo(f'Status: {response.status_code} Problem with the request. Ensure your input is a positive integer.\n\tExiting...')
                    else:
                        response = response.json()
                        ticket_data = response['ticket']
                        submitted_by = ticket_data['submitter_id']
                        created_at = ticket_data['created_at']
                        unparsed_submittime = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
                        month = unparsed_submittime.strftime("%m")
                        month_name = calendar.month_abbr[int(month)]
                        submit_time = unparsed_submittime.strftime(f"%d {month_name} %Y %H:%MHrs")
                        subject = ticket_data['subject']
                        body = ticket_data['description']
                        status = ticket_data['status'].upper()
                        click.echo(f"\n{status} ticket with Subject:'{subject}' opened by {submitted_by} at UTC {submit_time}")
                        click.echo(
                                    f"""--start of message--\n\n{body}--end of message--                                   
                                    """
                                  )
                except (requests.ConnectionError, requests.Timeout) as connectionError:
                    click.echo('Request timed out. Check your internet connection and try again!')    

    elif not retrievedOauthtoken():
        #authenticate flow
        if click.confirm('Are you sure you want to continue authentication? This will open a new window'):
            """View details of a ticket with user-provided id"""  #docstring

            authState = authenticate()
            if authState:                                                                                     #This is the authentication block. if user does not allow app access, exits
                context.invoke(ticket_detail)
            else:
                sys.exit("Authentication Failed\nExiting...")

        else:
            click.echo("Exiting...")

if __name__ == '__main__':
    ticket_detail_group()