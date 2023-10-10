#!/usr/bin/env python3
import argparse

#######################################
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input",type=str, help="Input file", default='')
parser.add_argument("-m", "--mode", type=str, help="Mode",      default='')

args        = parser.parse_args()
inputfile   = args.input
mode        = args.mode

# print(f'''Using input file {inputfile}''')

if mode!='filter' and mode!='alt':
    print('Invalid mode specified, exiting')
    exit(-1)

try:
    f = open(inputfile, 'r')
except:
    print(f'''Problem opening file {inputfile}''')
    exit(-2)

if mode == 'filter':
    for line in f:
        email = line.strip()
        split_mail = email.split('@')
        if split_mail[1] in ['jlab.org', 'anl.gov', 'bnl.gov', 'rcf.rhic.bnl.gov', 'doe.gov']: continue
        if '.gov' in split_mail[1]: continue
        print(email)


if mode == 'alt':
    for line in f:
        alt = line.strip().split(',')[1]
        if alt !='':
            print(alt)

        #split_mail = email.split('@')
        #if split_mail[1] in ['jlab.org', 'anl.gov', 'bnl.gov', 'rcf.rhic.bnl.gov', 'doe.gov']: continue
        #if '.gov' in split_mail[1]: continue
        #print(email)

exit(0)

