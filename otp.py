#!/usr/bin/env python2

import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='?')
args = parser.parse_args()

def readstdinbytes(size):
    keyorctextbk = sys.stdin.read(size)
    nf = open('keyorctextbk','w')
    nf.write(keyorctextbk)
    nf.close()
    return keyorctextbk

def padorunpad(text, padorunpadbytes):
    print ''.join([ chr(ord(a) ^ ord(b)) for a, b in zip(text, padorunpadbytes) ])

if __name__ == "__main__": 
    text = open(args.filename)
    text.seek(0,2)
    length = text.tell()
    text.seek(0,0)
    text = text.read()
    stdinbytes = readstdinbytes(length)
    padorunpad(text, stdinbytes)
