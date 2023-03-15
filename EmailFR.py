#!/usr/bin/python3
# -*- coding : utf-8  -*-

import sys
import re

file = open(sys.argv[1])
lines = file.readlines()
file.close()

genericemailpattern = r'\b.+@[A-Za-z0-9.-]+\.fr\b'
unauthorizedchars = ["&", "=", "_", "'", "-", "+", ",", ">", "<", "..", ".@"]

for line in lines : 
    for element in line.split(" ") : 
        element=element.strip()
        if re.match(genericemailpattern, element) and all(x not in element for x in unauthorizedchars) :
            print(element)
