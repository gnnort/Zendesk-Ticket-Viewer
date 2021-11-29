from click.testing import CliRunner
from main import all_tickets, ticket_detail
import unittest

class Ticket_detailTest(unittest.TestCase):

    def test_ticket_detail_SUCCESS(self):
        runner = CliRunner()
        test_string = "OPEN ticket with Subject:'Sample ticket: Meet the ticket' opened by 903435193506 at UTC 24 Nov 2021 06:54Hrs\n"
        result = runner.invoke(ticket_detail, ['--id', 1])
        self.assertEqual(result.output, test_string, "Should be equal")
        self.assertEqual(result.exit_code, 0, "Should be 0")
    
    def test_ticket_detail_INPUTERROR(self):
        runner = CliRunner()
        test_string = "Status: 400 Problem with the request. Ensure your input is a positive integer.\n\tExiting...\n"
        result = runner.invoke(ticket_detail, ['--id', 'f'], "Should be equal" )
        self.assertEqual(result.output, test_string)
    
    def test_ticket_detail_404ERROR(self):
        runner = CliRunner()
        test_string = 'Status: 404 ticket not found. Ensure the ticket id exists!\n'
        result = runner.invoke(ticket_detail, ['--id', 1000])
        self.assertEqual(result.output, test_string, "Should be equal")

    def test_ticket_detail_CLIENTERROR(self):
        runner = CliRunner()
        test_string = "Status: 400 Problem with the request. Ensure your input is a positive integer.\n\tExiting...\n"
        result = runner.invoke(ticket_detail, ['--id', -1])
        self.assertEqual(result.output, test_string, "Should be equal")

    def test_ticket_detail_CONNECTIONFAILED(self):
        pass #how to simulate no connection?
    def test_ticket_detail_SERVERERROR(self):
        pass


class View_all_ticketsTest(unittest.TestCase):

    def test_all_tickets_SUCCESS(self):
        runner = CliRunner()
        result = runner.invoke(all_tickets)
        self.assertEqual(result.exit_code, 0)
        #how do i test for this output?
    
    def test_view_all_tickets_CLIENTERROR(self):
        pass

    def test_view_all_tickets_SERVERERROR(self):
        pass



if __name__ == '__main__':
    unittest.main()