import click
import requests
import calendar
from datetime import datetime

user = "ngtron25@gmail.com/token"
pw = "IN5Kog01geHQSmjZ2cUN2N9dDCFEqBM1py59zrlW"

@click.group()
def ticket_detail_group():
    pass



@ticket_detail_group.command(options_metavar='<options>')
#@click.option('--id', help='Specify ID', metavar='<int>')
def ticket_detail():

    """View details of a ticket with user-provided id"""

    id = click.prompt('Please enter a valid Ticket ID', type=int)
    #ticket_id = id 
    url = "https://tron7825.zendesk.com/api/v2/tickets/" + str(id) + ".json"
    timeout = 8 #try to connect for 8s before timeout

    if not id: #if id is not specified by user, id value == None
        click.echo("Please specify ticket ID when using ticketdetails!")
    elif id < 0:
        click.echo("Please ensure your input is a positive integer\nExiting...")
    else:

        try:
            response = requests.get(url, auth=(user, pw), timeout=timeout)
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