#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Algorithm for selecting the best hypothesis using the internal python library.
To run the program , use the code:  -i testdata-small.csv -o result.csv.
The code works well for a small amount of data, for large sizes it is necessary to change the structure of the code to read.
Data occurred not entirely, but, for example, line by line.
At start in linux it is necessary to delete the encoding encoding = 'utf-8'.
"""

import getopt
import re
import sys
from difflib import SequenceMatcher

from translate import translate

# Coefficient that allows you to change the importance of the search criteria: by name and address
NAME_FACTOR = 1
ADDRESS_FACTOR = 1


def prepare_name(name):
    name = re.sub('"', '', name)
    name = re.sub("'", '', name)
    return name


# Function which, which leads the address to normal in view of
def prepare_address(address):
    transtable = (
        (r"\s\s+", " "),
        (r'\sул\.|ул\.\s|Ул\.\s?|\s?улица\s?|Улица\s|\sУл\.\s', ''),
        (r'\s?ш\.|\sШоссе\s?', ' шоссе '),
        (r'\sстр\.\b|\sстр\.\s|\sстр\s|\sСтр\.\s', ' ст'),
        (r'\sкорп\.|\sКорп\.|\sк\.', ' к'),
        (r'\sпл\.', ' площадь'),
        (r'\s?просп\.|\sПр-т|\sпр\.', ' проспект'),
        (r'\sд\.|\sД\.', ' '),
        (r'\sпр-д|\sПр\.|\sПр-д', ' проезд'),
        (r'\sбул\.|\sб-р', ' бульвар'),
        (r'\sпер\.|\sпереулок\s', ' пер'),
        (r'\sДом|\sДом\s|\sдом\s|\sд\s|\s?д\.|\s?Д\.', ' '),
        (r's\наб\.', ' набережная'),
    )
    for symb_in, symb_out in transtable:
        address = re.sub(symb_in, symb_out, address)
    address = translate(address)
    return address


def main(input_file_main, output_file_main):
    with open(input_file_main, 'r', encoding='utf-8') as f:
        with open(output_file_main, 'w', encoding='utf-8') as file_result:
            list_file = [line.split(';') for line in f]
            # Create a dictionary where the key is a unique id of the organization
            id_dict = {}
            for line in list_file:
                org_id = line[0]
                if org_id not in id_dict:
                    id_dict[org_id] = []
                id_dict[org_id].append(line)
            line_result = ''
            for org_id in id_dict:
                index = 0
                # Determines the best hypothesis
                for line_list_file in id_dict[org_id]:
                    ext_address = prepare_address(line_list_file[5])
                    ext_name = prepare_name(line_list_file[4])
                    # Using the standard difflib library
                    name_compare = SequenceMatcher(lambda x: x in ' "', line_list_file[1], ext_name)
                    address_compare = SequenceMatcher(lambda y: y in ' "', line_list_file[2], ext_address)
                    name_value = name_compare.ratio()
                    address_value = address_compare.ratio()
                    line_index = name_value * NAME_FACTOR + address_value * ADDRESS_FACTOR
                    if index <= line_index:
                        index = line_index
                        line_result = ';'.join(line_list_file)
                file_result.writelines(line_result)


if __name__ == '__main__':
    input_file = ''
    output_file = ''
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            input_file = arg
        elif opt in ('-o', '--ofile'):
            output_file = arg
    main(input_file, output_file)
