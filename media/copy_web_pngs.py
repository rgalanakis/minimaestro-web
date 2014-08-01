#!/usr/bin/python3
from __future__ import print_function
import os
import re
import shutil

THISDIR = os.path.dirname(__file__)
TARGET = os.path.join(THISDIR, '..', 'minimaestro', 'static', 'img')

def main():
    for tail in os.listdir(THISDIR):
        if re.match('.*_ss\d\.png', tail):
            src = os.path.join(THISDIR, tail)
            tgtname = tail.split('_')[-1]
            tgt = os.path.join(TARGET, tgtname)
            shutil.copyfile(src, tgt)
            print('Copied %s to %s' % (src, tgt))


if __name__ == '__main__':
    main()
