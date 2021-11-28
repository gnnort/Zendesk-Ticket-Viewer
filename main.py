import click
import requests
from datetime import datetime
import calendar

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
@click.option('--id')
def ticket_detail(id):
    ticket_id = id 
    url = "https://tron7825.zendesk.com/api/v2/tickets/" + str(ticket_id) + ".json"
    user = "ngtron25@gmail.com/token"
    pw = "IN5Kog01geHQSmjZ2cUN2N9dDCFEqBM1py59zrlW"
    response = requests.get(url, auth=(user, pw))
    if not id: #if id is not specified by user, id value == None
        print("Please specify ticket ID when using ticketdetails!")
    elif response.status_code > 299:
	    print('Status:', response.status_code, 'Problem with the request. Exiting...')
    else: #success
        response = response.json()
        data = response['ticket']
        submitted_by = data['submitter_id']
        created_at = data['created_at']
        submit_time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
        month = submit_time.strftime("%m")
        month_name = calendar.month_abbr[int(month)]
        new_format = f"%d {month_name} %Y %H:%MHrs"
        submit_time = submit_time.strftime(new_format)
        update_time = data['updated_at']
        subject = data['subject']
        status = data['status'].upper()
        print(f"{status} ticket with Subject:'{subject}' opened by {submitted_by} at UTC {submit_time}")

if __name__ == '__main__':
    cli()