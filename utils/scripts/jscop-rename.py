#!/usr/bin/env python
"""

"""

from __future__ import print_function

import sys
import os
import json

from argparse import ArgumentParser

#

if __name__ == '__main__':
    parser = ArgumentParser(description='Rename Polly JSCoP files')
    parser.add_argument(
        '-f',
        '--files',
        dest='jsonfiles',
        nargs='*',
        required=True,
        help='input JSON files')
    parser.add_argument(
        '-s',
        '--separator',
        dest='sep',
        default='-',
        help='separator for name components')
    parser.add_argument(
        '-e', '--extension', dest='ext', default='', help='filename extension')
    parser.add_argument(
        '-p', '--prefix', dest='prefix', default='', help='filename prefix')

    args = parser.parse_args()

    #

    rc = 0
    sep1 = '___'
    ext = args.ext

    for f in args.jsonfiles:
        lines = ''
        sourcefile = f

        if ext is '':
            _, ext = os.path.splitext(sourcefile)

        try:
            with open(f, "rb") as infile:
                j = json.load(infile)
                sourcefile, lines = j['location'].split(':')
        except OSError:
            rc = 2
            print('Could not open file: {}'.format(f))
        else:
            sourcefile = os.path.basename(sourcefile)
            funcname = f.split(sep1)[0]
            new_filename = '{}{}{}{}{}{}'.format(args.prefix, funcname, sep1,
                                                 sourcefile, args.sep, lines)

            suffix = ''
            attempt = 0
            max_attempts = 5
            while os.path.exists(new_filename + suffix +
                                 ext) and attempt < max_attempts:
                attempt = attempt + 1
                suffix = str(attempt)

            if attempt < max_attempts:
                new_filename += ext
                print('Renaming {} to {}'.format(f, new_filename))
                os.rename(f, new_filename)
            else:
                rc = 3
                print('Skipping file {} due to too many rename collisions'.
                      format(f))

    sys.exit(rc)
