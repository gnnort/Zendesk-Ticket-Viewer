from os import stat_result
import click
import requests
import calendar
from datetime import datetime

from oauth import authenticate, get_access_token, get_initial_code


@click.group()
def ticket_detail_group():
    pass


@ticket_detail_group.command()
def ticket_detail():

    if click.confirm('Are you sure you want to continue authentication? This will open a new window'):
        """View details of a ticket with user-provided id"""  #docstring
        
        header = authenticate()
        goodinput = False

        while goodinput == False:
            id = click.prompt('Please enter a valid Ticket ID')
            url = "https://tron7825.zendesk.com/api/v2/tickets/" + str(id) + ".json"

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
                    response = requests.get(url, headers = header, timeout=10)

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
                        status = ticket_data['status'].upper()
                        click.echo(f"{status} ticket with Subject:'{subject}' opened by {submitted_by} at UTC {submit_time}")


                except (requests.ConnectionError, requests.Timeout) as exception:
                    click.echo('Request timed out. Check your internet connection and try again!')


if __name__ == '__main__':
    ticket_detail_group()