#!/usr/bin/env python
import sys
import os
import re
import json
from psrd.universal import parse_universal
from psrd.options import exec_main, option_parser

def exec_main(parser, function, localdir):
	(options, args) = parser.parse_args()
	title = False
	if hasattr(options, 'title'):
		title = True

	if not options.output:
		sys.stderr.write("-o/--output required")
		sys.exit(1)
	if not os.path.exists(options.output):
		sys.stderr.write("-o/--output points to a directory that does not exist")
		sys.exit(1)
	if not os.path.isdir(options.output):
		sys.stderr.write("-o/--output points to a file, it must point to a directory")
		sys.exit(1)
	if not options.book:
		sys.stderr.write("-b/--book required")
		sys.exit(1)
	for arg in args:
		if title:
			parse_universal(arg, options.output, options.book, options.title)
		else:
			parse_universal(arg, options.output, options.book)

def main():
	usage = "usage: %prog [options] [filenames]\nParses files from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage, title=True)
	exec_main(parser, parse_rules, "rules")

if __name__ == "__main__":
	sys.exit(main())
