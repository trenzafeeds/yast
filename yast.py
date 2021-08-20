"""
yast.py
"""

from lib.window import *

def main(args):
    if len(args) > 1: main_window(args[1])
    else: main_window(None)
    return 0

if __name__ == '__main__':
    main(sys.argv)
