import argparse
from gift_exchange import GiftExchange


def get_file_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_path', type=str)
    args = parser.parse_args()
    return args.file_path


if __name__ == '__main__':
    file_path = get_file_path()
    if not file_path:
        print('Error: Must provide a file path with flag -f')
    else:
        gift_exchange = GiftExchange(file_path)
        match_list = gift_exchange.generate_match_list()
        gift_exchange.generate_csv(match_list)
