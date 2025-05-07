#!/bin/python
# -*- coding: utf-8 -*-

import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script executes a Hello World",  # main description for help
            epilog='Usage samples : \n\tpython klickbrick.py hello \n\n', formatter_class=argparse.RawTextHelpFormatter)  # displayed after help
#    parser.add_argument("-k", "--key",
#                        help="Mars ADS key",
#                        required=True)
