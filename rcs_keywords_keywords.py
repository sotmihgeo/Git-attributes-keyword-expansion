import os
import sys
import subprocess
import re

def gitdate():
    """Get the date from the latest commit in ISO8601 format."""
    args = ['git', 'log',  '-1', '--date=iso']
    lines = subprocess.check_output(args).splitlines()
    for l in lines:
        if l.startswith('Date:'):
            dat = l[5:].strip()
            return r'$Date: ' + dat + r' $'
    raise ValueError('Date not found in git output')

def gitrev():
    """Get the latest tag and use it as the revision number. This presumes the
    habit of using numerical tags.
    """
    args = ['git', 'describe',  '--tags']
    try:
        bitbucket = open('/dev/null')
        r = subprocess.check_output(args, stderr=bitbucket)[:-1]
        bitbucket.close()
    except subprocess.CalledProcessError:
        r = ''
    if len(r):
        return r'$Revision: ' + r + r' $'
    return r'$Revision: $'

## This is the main program ##
if __name__ == '__main__':
    currp = os.getcwd()
    if not os.path.exists(currp+'/.git'):
        print >> sys.stderr, 'This directory is not controlled by git!'
        sys.exit(1)
    date = gitdate()
    rev = gitrev()
    for line in sys.stdin:
        line = re.sub('\$Date\$', date, line)
        print re.sub('\$Revision\$', rev, line),