#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# import sys
import re
import os
import shutil
# import commands
import argparse
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    special_paths = []
    files = os.listdir(dir)
    for file in files:
        if re.search(r'__\w+__', file):
            special_paths.append(file)
    return special_paths


def copy_to(paths, dir):
    print('copy_to', paths, dir)


def zip_to(paths, zippath):
    print('zip_to', paths, zippath)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser(description='finds special files')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('fromdir', help='src dir to look for special files')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    if args.todir:
        for file in get_special_paths(args.fromdir):
            if not os.path.exists(args.todir):
                os.makedirs(args.todir)
            shutil.copy2(file, args.todir)
    if args.tozip:
        print("Command I'm going to do:")
        print('zip -j ' + args.tozip + ' ' +
              ' '.join(get_special_paths(args.fromdir)))
        subprocess.call(['zip', '-j', args.tozip] +
                        get_special_paths(args.fromdir))
    if not args.todir and not args.tozip:
        for file in get_special_paths(args.fromdir):
            print(os.path.abspath(file))


if __name__ == "__main__":
    main()
