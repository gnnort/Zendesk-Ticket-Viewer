import click
import requests
from datetime import datetime
from requests.models import Response
from oauth import authenticate




@click.group()
def all_tickets_group():
    pass


@all_tickets_group.command()
def all_tickets():
    if click.confirm('Are you sure you want to continue authentication? This will open a new window'):
        """View all tickets in account with 25 tickets per page"""

        header = authenticate()
        url = "https://tron7825.zendesk.com/api/v2/tickets" + ".json" + "?page[size]=25"                            #each page will have 25 tickets 
        page_count = 0

        while url:
            page_count += 1

            try:
                response = requests.get(url, headers= header, timeout= 10)
                if response.status_code >= 500:
                    click.echo('Status:', response.status_code, 'API is unavailable. Exiting...')
                elif response.status_code >= 400:
                    click.echo('Status:', response.status_code, 'Problem with the request. Exiting...')
                else:
                    data = response.json()                                                                          #decode to python dict
                    ticketList = []

                    for ticket in data['tickets']:                                                                  #data is a dictionary with 'tickets' as a key and a list of tickets as the value
                        ticketList.append(f"Ticket ID: {ticket['id']} Subject: '{ticket['subject']}'") 
                    click.echo(f"Page: {page_count}")
                    click.echo('\n'.join(ticketList))                                                               #every elem in list is joined by a new line
                    click.echo('\n')

                    if data['meta']['has_more']:                                                                    #cursor pagination
                        url = data['links']['next']
                    else:
                        url = None

            except (requests.ConnectionError, requests.Timeout) as exception:
                url = None
                click.echo('Request timed out. Check your internet connection and try again!')
    else:
        click.echo("Exiting...")


if __name__ == '__main__':
    all_tickets_group()