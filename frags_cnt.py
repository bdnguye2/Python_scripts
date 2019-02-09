#!/usr/bin/python3
#
# This script reads in csv file (user input) and 
# computes the total charge of fragments from
# Mulliken population analysis of the supermolecules.
# The csv file must be formatted with the following
# columns: Supermolecule, Monomer A, Monomer B. 
# In addition, the supermolecule coordinates must 
# have atoms organized starting with Monomer A 
# then Monomer B.
#
#
#

import csv
import numpy as np

filename = input('Enter the filename: ')

with open(filename,'r') as csv_file:
     mylist = []
     mylist2= []
     mylist3= []
     for i in csv.reader(csv_file, delimiter=','):
         mylist.append(i[0])
         mylist2.append(i[1])
         mylist3.append(i[2])
     mylist2 = list(filter(None, mylist2))
     mylist3 = list(filter(None, mylist3))

tmp=0
for i in mylist[1:len(mylist2)]:
    tmp += float(i)

tmp2=0
tot = len(mylist2)+len(mylist3)
for i in mylist[len(mylist2):]:
    tmp2 += float(i)

print('Total charge of monomer 1: ',tmp)
print('Total charge of monomer 2: ',tmp2)
