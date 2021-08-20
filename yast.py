"""
yast.py
"""
import window, sys

def main(args):
    if len(args) > 1: window.main_window(args[1])
    else: window.main_window(None)
    return 0

if __name__ == '__main__':
    main(sys.argv)
