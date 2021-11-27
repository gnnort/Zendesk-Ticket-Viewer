import click
import requests

@click.group()
def cli():
    "To be modified"

@cli.command()
def view_all_tickets():
    pass

@cli.command()
def ticket_detail():
    pass

if __name__ == '__main__':
    cli()