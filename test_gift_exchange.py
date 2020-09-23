import unittest

from gift_exchange import GiftExchange


class TestGiftExchange(unittest.TestCase):

    def setUp(self):
        self.mock_data = [
            {'name': 'Jane Doe', 'email': 'jane@example.com'},
            {'name': 'John Doe', 'email': 'joe@example.com'},
            {'name': 'Johnny Appleseed', 'email': 'johnny@example.com'},
        ]

        self.sender = {'name': 'Jane Doe', 'email': 'jane@example.com'}

    def test_get_match_is_not_self(self):
        """
        Unit test that `get_valid_match` is not the sender
        """
        gift_exchange = GiftExchange('mock/path')

        match = gift_exchange.get_valid_match_for_sender(
            self.mock_data, self.sender)

        # assert match is not sender
        self.assertNotEqual(
            self.sender.get('name'),
            match.get('name')
        )

    def test_get_match_is_marked_as_paired(self):
        """
        Unit test that `get_valid_match` has not already been picked
        """
        gift_exchange = GiftExchange('mock/path')
        gift_exchange.has_been_paired = ['John Doe']

        match = gift_exchange.get_valid_match_for_sender(
            self.mock_data, self.sender)

        # assert match is marked as paired
        self.assertFalse(match in gift_exchange.has_been_paired)

    def test_swap_picks(self):
        """
        Unit test edge case where we need to swap picks between 
        first and last sender
        """
        pick_to_switch = {'name': 'Foo Bar', 'email': 'foo@example.com'}

        gift_exchange = GiftExchange('mock/path')
        gift_exchange.paired_matches = {
            'Jane Doe': pick_to_switch,
            'John Doe': {},
        }

        last_sender = {
            'name': 'Baz Foo', 'email': 'baz@example.com'
        }

        match_before_swap = gift_exchange.paired_matches.get('Jane Doe')

        # first match is unchanged before swap
        self.assertEqual(
            match_before_swap.get('name'),
            pick_to_switch.get('name')
        )

        gift_exchange.swap_first_and_last_picks(last_sender)
        match_after_swap = gift_exchange.paired_matches.get('Jane Doe')
        last_sender_name = last_sender.get('name')

        # first match is switched after swap
        self.assertEqual(
            match_after_swap.get('name'),
            last_sender_name
        )

        last_match = gift_exchange.paired_matches.get(last_sender_name)

        self.assertEqual(
            last_match.get('name'),
            pick_to_switch.get('name')
        )


unittest.main(verbosity=2)
