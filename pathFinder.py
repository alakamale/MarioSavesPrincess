#######################################
# How to execute
# $ python pathFinder.py --glen <> --grid  <'' '' ''>
# e.g. python pathFinder.py --glen 3 --grid '--p' '--m' '--x'
#######################################

import argparse
from app import find_shortest_path

CLI=argparse.ArgumentParser()

CLI.add_argument(
  "--glen",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1,  # 0 or more values expected => creates a list
  type=int,
  default=[3],  # default if nothing is provided
)
CLI.add_argument(
  "--grid",
  nargs='*',
  type=str,  # any type/callable can be used here
  default=['--m','-x-','-p-'],
)

# parse the command line
args = CLI.parse_args()
# access CLI options
map = []
for i in range(len(args.grid)):
    map.append(args.grid[i].strip("'"))

try:
    print(find_shortest_path(args.glen[0], map))
except Exception as e:
    print(e)
    print("Invalid Grid!!! Please Try again.")


