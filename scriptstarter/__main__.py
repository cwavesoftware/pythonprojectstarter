import pathlib
import os
import argparse
import logging
import sys
import shutil

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')

parser = argparse.ArgumentParser(description='Creates a script with logging, argparse and other utilities ready')
parser.add_argument('name', metavar='name', help='Name of the script')
parser.add_argument('--desc', metavar='desc', help='Description of the script')

args = parser.parse_args()


if os.path.isfile(args.name):
    logging.error("The file already exists!\nNothing to do here")
    sys.exit(1)

templateFile = pathlib.Path(pathlib.Path(__file__).parent.resolve(), "template/template.py")

logging.info(f"Using template file {templateFile}")
if not args.desc:
    shutil.copyfile(templateFile, args.name)
else:
    with open(args.name, "w") as fout:
        with open(templateFile, "r") as fin:
            for line in fin:
                fout.write(line.replace("description='TBD'", f"description='{args.desc}'"))


logging.info("Done")