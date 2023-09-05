import pprint as pp

hs_baseline = {
    "CLASS_YEAR": 2020,
    "AC": 134,
    "PDS": 62,
    "EPTS": 18,
    "CD": 50
}

def hs(institution, roon):
    ref_dif = hs_baseline[institution] - roon
    result = {}
    for insti in hs_baseline.keys():
        result[insti] = hs_baseline[insti] - ref_dif
    return result
    
def hs_driver(input):
    parsed_input = input.split()
    return hs(parsed_input[0].upper(), int(parsed_input[1]))

if __name__ == "__main__":
    while True:
        input_txt = input("enter roon to convert: ")
        result = hs_driver(input_txt)
        pp.PrettyPrinter(width=20).pprint(result)