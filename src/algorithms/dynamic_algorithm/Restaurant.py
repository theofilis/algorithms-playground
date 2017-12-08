#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SYNOPSIS

    .

DESCRIPTION
    

EXAMPLES
    
    python baseclassifier.py filename.csv


EXIT STATUS
    
    0 program exit normal
    1 program had problem on execution


AUTHOR

    Theofilis George <theofilis.g@gmail.com>

LICENSE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

VERSION

    1
"""

import sys, os, traceback, optparse
import time
import re


def solve(p, m, k):

    def d(i):
        if i == 1:
            return p[i-1]
        else:
            subproblems = []

            for j in range(i-1, 0, -1):
                if ( sum( m[j-1:i-1] ) >= 200):
                    print i-1,j-1, sum( m[j-1:i-1] )
            subproblems += [p[i-1]]
            return max(subproblems + [d(i-1)])

    return d(len(p))

def main ():
    global options, args

    p = [1, 2, 3, 4]
    m = [200, 200, 200, 100]
    k = 200

    print solve(p, m, k)

if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
