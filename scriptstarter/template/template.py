import logging
import argparse

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a %d %b %Y %H:%M:%S')

parser = argparse.ArgumentParser(description='TBD')

args = parser.parse_args()

if __name__ == "__main__":
    logging.info("Done")