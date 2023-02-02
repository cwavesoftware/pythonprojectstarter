import logging
import argparse

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a %d %b %Y %H:%M:%S')

parser = argparse.ArgumentParser(description='TBD')
'''
# more examples here: https://docs.python.org/3/library/argparse.html

parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
'''
args = parser.parse_args()

if __name__ == "__main__":
    logging.info("Done")
