import pprint as pp
import csv
import sys

hs_baseline = {}

with open('hs_baseline.csv', 'r') as csvfile:
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

def mode_default():
    while True:
        input_txt = input("enter roon to convert: ")
        result = hs_driver(input_txt)
        pp.PrettyPrinter(width=20).pprint(result)

def mode_test(text):
    input_txt = text
    result = hs_driver(input_txt)
    pp.PrettyPrinter(width=20).pprint(result)

def mode_debug():
    mode_test("ac 134")
    mode_test("ac 135")
    mode_test("ac 132")

if __name__ == "__main__":
    if sys.argv[1] == '1':
        mode_debug()
    else:
        mode_default()