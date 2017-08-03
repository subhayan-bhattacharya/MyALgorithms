#!/usr/bin/env python3
# pyecho.py -- just echo our command line arguments

import sys

for arg in sys.argv[1:]:
    print(arg, end=' ')
print()



