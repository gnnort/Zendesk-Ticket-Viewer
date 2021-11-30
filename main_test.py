from click.testing import CliRunner
from main import all_tickets, ticket_detail


import unittest

class Ticketdetail_Test(unittest.TestCase):

    def test_ticket_detail_SUCCESS(self):
        runner = CliRunner()
        result = runner.invoke(ticket_detail, input= "1")
        self.assertEqual(result.exit_code, 0)
        self.assertFalse(result.exception)
    
    def test_ticket_detail_NOTPOSITIVEINTEGER(self):
        runner = CliRunner()
        test_string = "Please enter a valid Ticket ID: -10\nPlease ensure your input is a positive integer\nExiting...\n"
        result = runner.invoke(ticket_detail, input = '-10')
        self.assertEqual(result.output, test_string, "Should be equal")
        self.assertFalse(result.exception)


    def test_ticket_detail_404ERROR(self):
        runner = CliRunner()
        test_string = 'Please enter a valid Ticket ID: 1000\nStatus: 404 ticket not found. Ensure the ticket id exists!\n'
        result = runner.invoke(ticket_detail, input = '1000')
        self.assertFalse(result.exception)
        self.assertEqual(result.output, test_string, "Should be equal")
    

#     def test_ticket_detail_CONNECTIONFAILED(self):
#         pass #how to simulate no connection?
#     def test_ticket_detail_SERVERERROR(self):
#         pass


class AllTickets_Test(unittest.TestCase):

    def test_all_tickets_SUCCESS(self):
        runner = CliRunner()
        result = runner.invoke(all_tickets)
        self.assertEqual(result.exit_code, 0)
        self.assertFalse(result.exception)

    def test_all_tickets_EXTRAINPUT(self):
            runner = CliRunner()
            result = runner.invoke(all_tickets,['foo'])
            self.assertTrue(result.exception)
            self.assertEqual(result.exit_code, 2)
    
    def test_all_tickets_OPTION(self):
            runner = CliRunner()
            result = runner.invoke(all_tickets,['--foo', 'bar'])
            self.assertTrue(result.exception)
            self.assertEqual(result.exit_code, 2)
    
    
    def test_view_all_tickets_CLIENTERROR(self):
        pass

    def test_view_all_tickets_SERVERERROR(self):
        pass

#click exit_code:1 --> exception
# exit_code:2 --> Usage error. Program aborts
# exit_code:0 --> success

if __name__ == '__main__':
    unittest.main()