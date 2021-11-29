from click.testing import CliRunner
from main import view_all_tickets, ticket_detail

def test_ticket_detail():
    runner = CliRunner()
    test_string = "OPEN ticket with Subject:'Sample ticket: Meet the ticket' opened by 903435193506 at UTC 24 Nov 2021 06:54Hrs"
    result = runner.invoke(ticket_detail, ['--id', 1])
    assert result.exit_code == 0
    assert result.output == test_string + "\n"
test_ticket_detail()