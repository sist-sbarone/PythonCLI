#!/bin/python
# -*- coding: utf-8 -*-

import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script executes a Hello World",  # main description for help
            epilog='Usage samples : \n\tpython klickbrick.py hello \n\n', formatter_class=argparse.RawTextHelpFormatter)  # displayed after help
    subparsers = parser.add_subparsers(
    title="subcommands", help="hello commands")
    hello_parser = subparsers.add_parser("hello", help="hello message")
#    parser.add_argument("hello",
#                        help="Main argument")


    args = parser.parse_args()

    print("Hello World")