# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:47:37 2018

@author: mikey
"""

import os
import sys
sys.modules['itertools']
import csv

# Path to collect data from the folder
election_data_CSV = os.path.join('election_data_2.csv')


with open(election_data_CSV, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    votingResults = {row[1]: row[0], row[2] for rows in csvreader}

print(votingResults)