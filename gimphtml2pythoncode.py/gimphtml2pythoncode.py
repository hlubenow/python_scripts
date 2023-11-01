#!/usr/bin/python
# coding: utf-8

import sys

"""
    gimphtml2pythoncode.py 1.0 - Convert a gimp (sprite-) image, that's exported as "HTML table", to Python code.

    Copyright (C) 2023 Hauke Lubenow

    This program is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

def getColornumbers(a):
    hexvals = {}
    for i in range(10, 16): 
        hexvals[i] = chr(i + 55)
    colornumbers = {}
    n = 0
    for i in a:
        i = i.strip()
        if "BGCOLOR" in i:
            c = i.split("BGCOLOR=#")
            colornumber = c[1].rstrip(">")
            if not colornumber in colornumbers:
                if n < 10:
                    colornumbers[colornumber] = str(n)
                elif n >= 10 and n <= 15:
                    colornumbers[colornumber] = str(hexvals[n])
                else:
                    print("\nError: More than 16 colors.\n")
                    sys.exit(1)
                n += 1
    if "000000" in colornumbers:
        for i in colornumbers:
            if colornumbers[i] == "0":
                temp = colornumbers["000000"]
                colornumbers["000000"] = "0"
                colornumbers[i] = temp
                break
    return colornumbers

def toPprint(a, firstline):
    b = []
    for i in range(len(a)):
        if i == 0:
            s = firstline + '"' + a[i] + '"'
            if len(a) > 1:
                s += ","
            b.append(s)
            continue
        s = len(firstline) * " " + '"' + a[i] + '"'
        if i < len(a) - 1:
            s += ","
        else:
            s += ")"
        b.append(s)
    return b

# Main

if len(sys.argv) < 2:
    print "\nUsage: gimphtml2pythoncode.py [gimpimagefile.html]\n"
    sys.exit(1)

fh = open(sys.argv[1], "r")
a = fh.readlines()
fh.close()

colornumbers = getColornumbers(a)

b = []
s = ""
for i in a:
    i = i.strip()
    if "TABLE" in i:
        continue
    if "BGCOLOR" in i:
        c = i.split("BGCOLOR=#")
        colornumber = c[1].rstrip(">")
        for u in colornumbers:
            if colornumber == u:
                s += colornumbers[u]
    if i == "</TR>":
        b.append(s)
        s = ""

b = toPprint(b, "spritedata = (")

header = ("#!/usr/bin/python", "")

for i in header:
    print i

for i in b:
    print i
