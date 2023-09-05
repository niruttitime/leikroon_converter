import pprint as pp
import csv
import sys

hs_baseline = {}

with open('hs_baseline.tsv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='\t')
    for row in csv_reader:
        hs_baseline[row[0].upper()] = int(row[1])

def hs(institution, roon):
    ref_dif = hs_baseline[institution] - roon
    result = {}
    for insti in hs_baseline.keys():
        result[insti] = hs_baseline[insti] - ref_dif
    return result
    
def hs_driver(input):
    parsed_input = input.split()
    return hs(parsed_input[0].upper(), int(parsed_input[1]))

def mode_arg(text):
    input_txt = text
    result = hs_driver(input_txt)
    pp.PrettyPrinter(width=20).pprint(result)

def mode_debug():
    mode_arg("ac 134")
    print() # eye break
    mode_arg("ac 135")
    print() # eye break
    mode_arg("ac 132")

def mode_single():
    input_txt = input("enter roon to convert: ")
    mode_arg(input_txt)


def mode_default():
    while True:
        input_txt = input("enter roon to convert: ")
        result = hs_driver(input_txt)
        pp.PrettyPrinter(width=20).pprint(result)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        mode_single()
    elif sys.argv[1] == '1':
        mode_debug()
    elif sys.argv[1] == '0':
        mode_default()
    else:
        mode_single()