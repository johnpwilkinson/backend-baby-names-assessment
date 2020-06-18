#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

import sys
import re
import argparse


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    names = []
    result_dict = {}
    with open(filename, 'r') as f:
        f_contents = f.read()
        # finditer returns an iterator of match objects for the PATTERN in the STRING
        for match in re.finditer(r'in \d{4}',f_contents ):
            # match.span returns a 2-tuple of the index of the match in the file
            year = match.span()
            # makes a slice from f_contents based on the index tuple to capture the year
            # and adds it to the names list 
            names.append(f_contents[year[1]-4:year[1]])
    # find all names on the page
        name_and_ranking=re.findall(r'"right"><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>', f_contents)
        for name in name_and_ranking:
            # if the names are not in the dict, then add them and set their rankings as their values
            if not name[1] in result_dict:
                result_dict[name[1]]=name[0]
            if not name[2] in result_dict:
                result_dict[name[2]]=name[0]
            # sort the keys alphabetically and unpack them and their values... add them to names list
        for key, value in sorted(result_dict.items()):
            names.append(key + ' ' + value)
    return names



def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    # +++your code here+++
    for file in file_list:
        _file = extract_names(file)
        if not create_summary:
            print(*_file, sep='\n')
        else:
            summary_file = file + '.summary'
            with open(summary_file, 'w') as j:
                for data in _file:
                    j.write(data + '\n')

if __name__ == '__main__':
    main(sys.argv[1:])
