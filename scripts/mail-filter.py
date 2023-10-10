#!/usr/bin/env python3
import csv
import argparse


#######################################
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",  action='store_true', help="Verbose mode")
parser.add_argument("-i", "--input",type=str, help="Input file", default='')

args        = parser.parse_args()
inputfile   = args.input

print(f'''Using input file {inputfile}''')

f = open(inputfile, 'r')

for line in f:
    email = line.strip()
    split_mail = email.split('@')
    if split_mail[1] in ['jlab.org', 'anl.gov', 'bnl.gov', 'rcf.rhic.bnl.gov', 'doe.gov']: continue
    if '.gov' in split_mail[1]: continue
    print(email)
exit(0)

