import click
import requests
from datetime import datetime
import calendar

user = "ngtron25@gmail.com/token"
pw = "IN5Kog01geHQSmjZ2cUN2N9dDCFEqBM1py59zrlW"

@click.group()
def cli():
    """
    \b
      =%%%%%%%%%%%#  #%%%%%%%%%%%=      
       :%%%%%%%%%%#  #%%%%%%%%%%:       
         :%%%%%%%%#  #%%%%%%%%:         
            ---   ,  #%%%%%%:          
                :%#  #%%%%%:            
              :%%%#  #%%%:              
             :%%%%#  #%:               
            :%%%%%#  `     __          
          :%%%%%%%#     :%%%%%%:       
        :%%%%%%%%%#   :%%%%%%%%%%:     
       :%%%%%%%%%%#  :%%%%%%%%%%%%:
       
Welcome to the Zendesk Ticket Viewer!
Type python main.py <command> to use
Use python main.py <command> --help for detailed instructions on each command    
    """   

@cli.command()
def all_tickets():
    """View all tickets in account with 25 tickets per page"""
    url = "https://tron7825.zendesk.com/api/v2/tickets" + ".json" + "?page[size]=25"   #each page will have 25 tickets #what is the .json for?
    page_count = 0
    while url:
        page_count += 1
        try:
            response = requests.get(url, auth= (user,pw))
            if response.status_code >= 500:
	            print('Status:', response.status_code, 'API is unavailable. Exiting...')
            elif response.status_code >= 400:
	            print('Status:', response.status_code, 'Problem with the request. Exiting...')
            else:
                data = response.json() #decode to python dict
                ticketList = []
                for ticket in data['tickets']: #data is a dictionary with 'tickets' as a key and a list of tickets as the value
                    ticketList.append(f"Ticket ID: {ticket['id']} Subject: '{ticket['subject']}'") #convert to fstring?
                click.echo(f"Page: {page_count}")
                click.echo('\n'.join(ticketList)) #every elem in list is joined by a new line
                click.echo('\n')
                if data['meta']['has_more']:  #cursor pagination
                    url = data['links']['next']
                else:
                    url = None
        except (requests.ConnectionError, requests.Timeout) as exception:
            url = None
            print('Request timed out. Check your internet connection and try again!')

@cli.command(options_metavar='<options>')
@click.option('--id', help='Specify ID', metavar='<int>')
def ticket_detail(id):
    """View details of a ticket with user-provided id"""
    ticket_id = id 
    url = "https://tron7825.zendesk.com/api/v2/tickets/" + str(ticket_id) + ".json"
    timeout = 8 #try to connect for 8s before timeout
    if not id: #if id is not specified by user, id value == None
        print("Please specify ticket ID when using ticketdetails!")
    else:
        try:
            response = requests.get(url, auth=(user, pw), timeout=timeout)
            if response.status_code >= 500:
	            print('Status:', response.status_code, 'API is unavailable. Exiting...')
            elif response.status_code >= 400:
	            print('Status:', response.status_code, 'Problem with the request. Ensure your input is a positive integer. Exiting...')
            else:
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
                click.echo(f"{status} ticket with Subject:'{subject}' opened by {submitted_by} at UTC {submit_time}")

        except (requests.ConnectionError, requests.Timeout) as exception:
            print('Request timed out. Check your internet connection and try again!')

if __name__ == '__main__':
    cli()
