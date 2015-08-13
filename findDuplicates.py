#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, argparse

"""
This script will read n iso2709 files and find any record that is present in multiple
files
"""

from pymarc import MARCReader, marc8_to_unicode

parser = argparse.ArgumentParser(description='Read an iso2709 file and display it in a mnemonic format.')

parser.add_argument('filename', nargs='*')
args = parser.parse_args()

files = {}

common = {}
for f in args.filename:
	print "******************************\nOpening %s" % f
	files[f] = {}
	files[f]['name'] = f
	files[f]['identifiers'] = {}
	
	nb = 0
	reader = MARCReader(open(f));
	for record in reader:
		nb += 1
		f001 = record.get_fields("001")[0]
		v001 = f001.value()
		
		if v001 in common:
			common[v001][f] = 1
		else:
			common[v001] = {}
			common[v001][f] = 1
		files[f]['identifiers'][v001] = 1
	print "> %s records" % nb

print "\n***   Analyze duplicates   ***"
nb = 0
for v001 in common:
	# Clean the values in files to be able to identify uniqueness of each file
	if len(common[v001]) > 1:
		for f in files:
			if v001 in files[f]['identifiers']:
				del(files[f]['identifiers'][v001])

		# print nb, ":", v001, len(common[v001])
		nb += 1

print "> Total number of ID: %s" % len(common)
print "> ID common between at least 2 files: %s" % nb

print "> Uniqueness for each file :"
for f in files:
	print "\t%s : %s record(s)" % (f, len(files[f]['identifiers']))

exit()

filename = args.filename

print "Opening %s" % filename
outputedLines = 0
for field in record:
	fieldValue = field.__str__().encode("utf-8")
	if "\n" in fieldValue:
		print "Carriage return in record #%s (%s field)" % (nb, field.tag)

nb += 1

print "%s records in file" % (nb - 1)
