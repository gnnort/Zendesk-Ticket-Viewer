from click.testing import CliRunner
from main import view_all_tickets, ticket_detail
import unittest

class Ticket_detailTest(unittest.TestCase):

    def test_ticket_detail_SUCCESS(self):
        runner = CliRunner()
        test_string = "OPEN ticket with Subject:'Sample ticket: Meet the ticket' opened by 903435193506 at UTC 24 Nov 2021 06:54Hrs\n"
        result = runner.invoke(ticket_detail, ['--id', 1])
        self.assertEqual(result.output, test_string, "Should be equal")
        self.assertEqual(result.exit_code, 0, "Should be 0")
    
    def test_ticket_detail_CLIENTERROR(self):
        runner = CliRunner()
        test_string = "Status: 400 Problem with the request. Exiting...\n"
        result = runner.invoke(ticket_detail, ['--id', -1])
        self.assertEqual(result.output, test_string, "Should be equal")

    def test_ticket_detail_SERVERERROR(self):
        pass


class View_all_ticketsTest(unittest.TestCase):

    def test_view_all_tickets_SUCCESS(self):
        runner = CliRunner()
        result = runner.invoke(view_all_tickets)
        self.assertEqual(result.exit_code, 0)
        #how do i test for this output?
    
    def test_view_all_tickets_CLIENTERROR(self):
        pass

    def test_view_all_tickets_SERVERERROR(self):
        pass



if __name__ == '__main__':
    unittest.main()