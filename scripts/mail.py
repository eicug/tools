#!/usr/bin/env python3

import csv


with open("eicug-members.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        alt_email = row["alternate e-mail"]
        if alt_email != '':
            print(alt_email)
        else:
            email = row["e-mail"]
            split_mail = email.split('@')
            if split_mail[1] in ['jlab.org', 'anl.gov', 'bnl.gov', 'rcf.rhic.bnl.gov', 'doe.gov']: continue

            if '.gov' in split_mail[1]: continue
            print(email)


 # jlab.org or anl.gov or bnl.gov or doe.gov
