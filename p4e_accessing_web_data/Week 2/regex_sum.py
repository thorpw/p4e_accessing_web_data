#!/usr/bin/env python

import re

with open("regex_sum_98385.txt") as f:
    x = f.read()

integers = re.findall('[0-9]+',x)

print(sum(int(i) for i in integers))
