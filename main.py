import click
import requests

@click.group()
def cli():
    "To be modified"

@cli.command()
def view_all_tickets():
    url = "https://tron7825.zendesk.com/api/v2/tickets" + ".json" + "?page[size]=25"   #each page will have 25 tickets #what is the .json for?
    user = "ngtron25@gmail.com/token"
    pw = "IN5Kog01geHQSmjZ2cUN2N9dDCFEqBM1py59zrlW"
    page_count = 0
    while url:
        page_count += 1
        response = requests.get(url, auth= (user,pw))
        data = response.json() #decode to python dict
        if response.status_code > 299:
            print("Error", response.status_code)
            quit
        else:
            ticketList = []
            for ticket in data['tickets']: #data is a dictionary with 'tickets' as a key and a list of tickets as the value
                ticketList.append("Subject: " + "-" + ticket['subject'] + "-" + " Ticket ID is " + str(ticket['id'])) #convert to fstring?
            print(f"Page: {page_count}")
            print('\n'.join(ticketList)) #every elem in list is joined by a new line
            print('\n')
            if data['meta']['has_more']:  #cursor pagination
                url = data['links']['next']
            else:
                url = None

@cli.command()
def ticket_detail():
    pass

if __name__ == '__main__':
    cli()