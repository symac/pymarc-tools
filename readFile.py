﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, argparse
#reload(sys)
#sys.setdefaultencoding('utf8')

"""
This script will read an iso2709 file and display it using mnemonics codes. This hasn't been widely tested and there should be issues with encodings.
"""

from pymarc import MARCReader, marc8_to_unicode

parser = argparse.ArgumentParser(description='Read an iso2709 file and display it in a mnemonic format.')

parser.add_argument('filename')
parser.add_argument('-tag',  default="", help='A tag to filter the output')
args = parser.parse_args()

filename = args.filename
tagFilter = args.tag
print "Opening %s" % filename
nb = 1
reader = MARCReader(open(filename));

for record in reader:
	print "\n##### RECORD %s #####" % nb
	for field in [x for x in record if (tagFilter == "" or x.tag == tagFilter)]:
		fieldValue = field.__str__().encode("utf-8")
		print fieldValue
	nb += 1

print "%s records in file" % nb