#!/bin/python
# -*- coding: utf-8 -*-

import argparse

def hello(target):
    hello_target = target if target else 'World'
    return "Hello %s" % hello_target

    
def start():
    parser = argparse.ArgumentParser(description="This script executes a Hello World",  # main description for help
            epilog='Usage samples : \n\tpython klickbrick.py hello \n\n', formatter_class=argparse.RawTextHelpFormatter)  # displayed after help
    subparsers = parser.add_subparsers(
    title="subcommands", help="hello commands")
    hello_parser = subparsers.add_parser("hello", help="hello message")
    hello_parser.add_argument("-n", "--name",
                        help="Your name ",
                        required=False)



    args = parser.parse_args()
    print(hello(args.name))
    exit(0)

if __name__ == "__main__":
    start()