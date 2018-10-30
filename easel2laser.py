#!/usr/bin/env python

import sys

lines = []
result = []

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

for line in lines:
    if 'M3' in line or 'M4' in line:
        continue

    if 'Z-1' in line:
        result.append(line)
        result.append('M3 S' + sys.argv[3] + '\n')

    elif 'Z1' in line:
        result.append('M3 S' + sys.argv[4] + '\n')
        result.append(line)

    else:
        result.append(line)

with open(sys.argv[2], 'w') as f:
    for line in result:
        f.write(line);
