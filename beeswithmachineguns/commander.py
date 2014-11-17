#!/usr/bin/env python

import subprocess
from optparse import OptionParser

def run_command(line):
    if not line:
        return False

    line = line.strip()
    if not line or line[0] == '#':
        return False

    print 'run command: %s =>' % line

    cmd = 'bees ' + line

    ## run it ##
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
 
    ## But do not wait till netstat finish, start displaying output immediately ##
    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            break
            if out != '':
                sys.stdout.write(out)
                sys.stdout.flush()
            
    return True

def parse_options():
    """
    Launch bees to execute commands based on command list from file
    """
    parser = OptionParser(usage="""
    commander [fileName]
    """)

    print 'heelo'

    (options, args) = parser.parse_args()

    print len(args), 'args.length'
    
    if len(args) <= 0:
        parser.error('Please provide the command text file name.')

    file_name = args[0]
    f = open(file_name, 'r')
    
    for line in f:
        run_command(line)

    f.close()
        
def main():
    parse_options();


if __name__ == '__main__':
    main()
