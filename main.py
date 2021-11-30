import click

from commands.ticket_detail import ticket_detail
from commands.all_tickets import all_tickets


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

#commands 
cli.add_command(ticket_detail)
cli.add_command(all_tickets)


if __name__ == '__main__':
    cli()
