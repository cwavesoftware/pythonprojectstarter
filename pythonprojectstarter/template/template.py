import logging
import argparse

parser = argparse.ArgumentParser(description='TBD')
parser.add_argument('--log-level')
'''
# more examples here: https://docs.python.org/3/library/argparse.html

parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
'''
args = parser.parse_args()

if args.log_level == 'debug':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a %d %b %Y %H:%M:%S')
elif args.log_level == 'info':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a %d %b %Y %H:%M:%S')
elif args.log_level == 'warning':
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a %d %b %Y %H:%M:%S')
elif args.log_level == 'error':
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a %d %b %Y %H:%M:%S')

if __name__ == "__main__":
    logging.info("Done")
