#!/usr/bin/env python
"""

"""

from __future__ import print_function

import sys
import os
import json

from ruamel.yaml import YAML
from argparse import ArgumentParser

#

if __name__ == '__main__':
    parser = ArgumentParser(description='Convert YAML to JSON files')
    parser.add_argument(
        '-f',
        '--files',
        dest='files',
        nargs='*',
        required=True,
        help='input YAML files')

    args = parser.parse_args()

    #

    rc = 0
    yaml = YAML()

    for fname in args.files:
        name, ext = os.path.splitext(fname)
        outfname = name + ".json"

        try:
            with open(fname, "rb") as infile, open(outfname, "wb") as outfile:
                objs = yaml.load_all(infile)
                for o in objs:
                    json.dump(o, outfile, indent=2)
        except OSError:
            rc = 2
            print('Could not open files: {}, {}'.format(fname, outfname))

    sys.exit(rc)
