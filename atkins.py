#!/usr/bin/python3

from functools import reduce
from sys import stderr, exit

import argparse

from parser import parser
from parser import Node_Types

arg_parse = argparse.ArgumentParser()

arg_parse.add_argument("project")
arg_parse.add_argument("-M", help="Print project dependencies to stdout", action="store_true")
args = arg_parse.parse_args()

if not args.project:
	exit(1)

project = args.project
target_base = project.split('.')[0]

target = "%s, %s.d : " % (project, target_base)

with open(project) as file:
	data = file.read()
	p = parser.parse(data, debug=False)

target = "test.gpj test.d : "

is_dependency = lambda x: x[0] == Node_Types.FILENAME
make_list = lambda x, y: x + y[1] + " "

output = reduce(make_list,filter(is_dependency, p), target)

if args.M:
	print(output)
