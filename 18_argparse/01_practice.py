# Argparse 教學 : https://docs.python.org/zh-tw/3/howto/argparse.html

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
