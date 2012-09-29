import re
import string
import sys
if len(sys.argv) < 2:
    sys.stderr.write('Usage: sys.argv[0]\n')
elif len(sys.argv) == 3:
    f = open(sys.argv[1], 'r')
    o = open(sys.argv[2], 'w')
    line = f.readline()
    while line:
        match = re.match(".* (?P<comparator>[><]) .*", line)
        if match:
            print line
            comparator = match.group("comparator") 
            print comparator
            newline = re.sub(' ([><]) ', " \\"+comparator+" ", line)
            print newline
            o.write(newline)
        else:
            o.write(line)
        line = f.readline()

