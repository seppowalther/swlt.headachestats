# CSV-Output Format
import csv
testlist = []
with open('output.csv', newline='') as csvfile:
    test = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in test:
        testlist.append(', '.join(row))

testlist_splitted = testlist[3].split(',')

import pdb; pdb.set_trace()