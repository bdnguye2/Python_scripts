#!/usr/bin/python3
#
# This script reads in csv file (user input) and 
# computes the total charge of molecule from
# Mulliken population analysis
#
#

import csv

filename = input('Enter the filename: ')
column = input('Enter the column e.g 1: ')
with open(filename,newline='') as csv_file:
     mylist = []
     for i in csv.reader(csv_file, delimiter=','):
         mylist.append(i[int(column)-1])
     mylist = list(filter(None, mylist))

tmp=0
for i in mylist[1:]:
    tmp += float(i)

print(tmp)
