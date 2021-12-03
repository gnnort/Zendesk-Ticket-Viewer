from click.testing import CliRunner
import unittest
from unittest import mock
from main import all_tickets, ticket_detail



class Ticketdetail_Test(unittest.TestCase):
    def setUp(self):                                                                                         #Cases where user confirms authentication but auth fails go here
        self.confirm = mock.patch('commands.ticket_detail.click.confirm', return_value=True)
        self.confirm.start()
        self.authenticate = mock.patch('commands.ticket_detail.authenticate', return_value= False)
        self.authenticate.start()

    def test_ticket_detail_AUTHFAIL(self):
        exitstring = "Authentication Failed\nExiting...\n"
        runner = CliRunner()
        result = runner.invoke(ticket_detail)
        self.assertEqual(result.output, exitstring)   

    def tearDown(self):                                                                                       #end here
        self.confirm.stop()
        self.authenticate.stop()


    def test_ticket_detail_USERREFUSESAUTH(self):
        exitstring = "Exiting...\n"
        runner = CliRunner()
        with mock.patch('commands.ticket_detail.click.confirm', return_value=False):
            result = runner.invoke(ticket_detail)
            self.assertEqual(result.output, exitstring)

class AllTickets_Test(unittest.TestCase):

    def setUp(self):                                                                                         #Cases where user confirms authentication but auth fails go here
        self.confirm = mock.patch('commands.all_tickets.click.confirm', return_value=True)
        self.confirm.start()
        self.authenticate = mock.patch('commands.all_tickets.authenticate', return_value= False)
        self.authenticate.start()

    def test_all_tickets_AUTHFAIL(self):
        exitstring = "Exiting...\n"
        runner = CliRunner()
        result = runner.invoke(all_tickets)
        self.assertEqual(result.output, exitstring)   

    def tearDown(self):                                                                                       #end here
        self.confirm.stop()
        self.authenticate.stop()


    def test_all_tickets_EXTRAINPUT(self):
            runner = CliRunner()
            result = runner.invoke(all_tickets,['foo'])
            self.assertTrue(result.exception)
            self.assertEqual(result.exit_code, 2)
    
    def test_all_tickets_WRONGOPTION(self):
            runner = CliRunner()
            result = runner.invoke(all_tickets,['--foo', 'bar'])
            self.assertTrue(result.exception)
            self.assertEqual(result.exit_code, 2)
    

    def test_all_tickets_USERREFUSESAUTH(self):
        exitstring = "Exiting...\n"
        runner = CliRunner()

        with mock.patch('commands.all_tickets.click.confirm', return_value=False):
            result = runner.invoke(all_tickets)
            self.assertEqual(result.output, exitstring)

    

#click exit_code:1 --> exception
# exit_code:2 --> Usage error. Program aborts
# exit_code:0 --> success

if __name__ == '__main__':
    unittest.main()