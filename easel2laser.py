#!/usr/bin/env python

import sys

lines = []
result = []

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

for line in lines:
    if 'M3' in line or 'M4' in line:
        continue

    # turn on laser
    if 'Z-' in line:
        result.append('M3 S' + sys.argv[3] + '\n')

    # turn off laser
    elif 'Z' in line:
        result.append('M3 S' + sys.argv[4] + '\n')

    else:
        result.append(line)

with open(sys.argv[2], 'w') as f:
    for line in result:
        f.write(line);
