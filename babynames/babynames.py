#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    rank_dict = dict()
    with open(filename, 'r') as file:
        file_contents = file.read()
        year = re.findall(r'Popularity in ([0-9]{4})', file_contents)
        for elem in re.finditer(
                r'<td>(?P<rank>\d+)</td><td>(?P<male_name>\w+)</td><td>(?P<female_name>\w+)</td>',
                file_contents):
            rank_dict[elem.group('male_name')] = elem.group('rank')
            rank_dict[elem.group('female_name')] = elem.group('rank')

    return year + ["{} {}".format(k, rank_dict[k]) for k in sorted(rank_dict)]


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    for filename in args:
        if summary:
            with open('summary.log', 'a') as summary_file:
                for elem in extract_names(filename):
                    summary_file.write("{}\n".format(elem))
        else:
            print(extract_names(filename))
        # For each filename, get the names, then either print the text output
        # or write it to a summary file


if __name__ == '__main__':
    main()
