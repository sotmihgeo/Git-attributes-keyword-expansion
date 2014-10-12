import sys
import re

if __name__ == '__main__':
    dre = re.compile(''.join([r'\$', r'Date.*\$']))
    drep = ''.join(['$', 'Date', '$'])
    rre = re.compile(''.join([r'\$', r'Revision.*\$']))
    rrep = ''.join(['$', 'Revision', '$'])
    for line in sys.stdin:
        line = dre.sub(drep, line)
        print rre.sub(rrep, line),