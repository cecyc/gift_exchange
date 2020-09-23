import csv
import copy
import datetime
import random


class GiftExchange:
    def __init__(self, file_path):
        self.file_path = file_path
        self.paired_matches = {}
        self.has_been_paired = []

    def get_csv_data(self):
        """
        Returns CSV data as an Array of Dicts
        Keys in Dict are the CSV headers
        """
        csv_data = []
        with open(self.file_path) as csvfile:
            csvfile = csv.DictReader(csvfile)
            for row in csvfile:
                csv_data.append(row)
        return csv_data

    def generate_csv(self, match_list):
        """
        Writes a CSV to root with today's date
        as the file name
        """
        file_date = datetime.date.today().strftime('%Y-%m-%d')
        csv_name = 'gift-exchange-matches-{}.csv'.format(file_date)
        with open(csv_name, 'w+') as csv_file:
            csvwriter = csv.writer(csv_file)

            # write header row
            csvwriter.writerow(['sender', 'match_name', 'match_email'])

            # write matches to csv
            for sender in match_list.keys():
                match = match_list.get(sender)
                match_name = match.get('name')
                match_email = match.get('email')
                csvwriter.writerow([sender, match_name, match_email])

    def get_valid_match_for_sender(self, csv_data, sender):
        """
        Return valid match for sender. A valid match is not
        the sender, and has not already been paired.

        Parameters:
        -----------
        csv_data (Array): Array of Dict data from CSV
        sender (Dict): Dict of individual sender

        Returns:
        --------
        valid_match (Dict): Dict of matched person
        """

        # copy csv data so we don't mutate it
        csv_data_cp = copy.copy(csv_data)

        # remove sender from pool
        csv_data_cp.remove(sender)

        # get max index for range
        data_len = len(csv_data_cp) - 1

        valid_match = None
        while not valid_match:
            random_match_index = random.randint(0, data_len)
            match = csv_data_cp[random_match_index]
            match_name = match.get('name')

            if match_name not in self.has_been_paired:
                valid_match = match
                self.has_been_paired.append(match_name)

        return valid_match

    def generate_match_list(self):
        """
        Returns Array of Dicts where key is sender, and value
        is a Dict of the person they paired with
        """
        csv_data = self.get_csv_data()
        last_item_index = len(csv_data) - 1
        for (idx, sender) in enumerate(csv_data):
            sender_name = sender.get('name')

            # if last item can only be paired with itself
            # swap pick with first pick
            not_paired = sender_name not in self.has_been_paired
            if idx == last_item_index and not_paired:
                self.swap_first_and_last_picks(sender)
            else:
                match = self.get_valid_match_for_sender(csv_data, sender)
                self.paired_matches[sender_name] = match

        return self.paired_matches

    def get_first_match_name(self):
        """
        Return first item in paired matches
        """
        return list(self.paired_matches.keys())[0]

    def swap_first_and_last_picks(self, sender):
        """
        Fix edge case where last match could only be paired
        with itself.

        By this point, we know that matches cannot be the sender,
        and matches cannot already have been picked. 

        If we hit this edge case, we know this is the last match,
        so we swap for the first sender's match.
        """
        sender_name = sender.get('name')
        first_match_name = self.get_first_match_name()
        first_match_pick = self.paired_matches.get(first_match_name)
        self.paired_matches[sender_name] = first_match_pick
        self.paired_matches[first_match_name] = sender
