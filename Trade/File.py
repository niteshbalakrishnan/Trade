import csv
import sys
import 
class CsvFile:

    def readfile (self , filename):

        with open(filename,newline='') as csvfile:
            sp = csv.reader(csvfile)
            for row in sp:
                print(row[0])
                print(', '.join(row))


        return 1

sys

