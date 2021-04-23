#this might not need it's own file lmao

import csv

#no need for a lexer as the csvreader does it automatically
def read(fname):
    tmp = [n for n in csv.reader(open(fname, "r"), delimiter=" ")]
    return tmp
