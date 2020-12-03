# https://www.programcreek.com/python/example/100428/oauth2client.tools.argparser 

#part 1

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
    

# part 2

import argparse

class C:
    pass

c = C()
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.parse_args(args=['--foo', 'BAR'], namespace=c)
c.foo
