#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""

  import re

  with open(filename, 'r') as f:
      # match any non word or non whitespace
      word_list = re.sub('[^\w\s]', '', f.read()).strip().lower().split()

      # kick start
      mimic_dict = {'': [word_list[0]]}

      for i in range(0, len(word_list)-1):
          word = word_list[i]
          words_next = mimic_dict.get(word, [])
          words_next.append(word_list[i+1])
          mimic_dict[word] = words_next

      # work around, last word -> first one
      mimic_dict[word_list[-1]] = [word_list[0]]

  return mimic_dict


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  mimic_words = list()
  while(len(mimic_words) < 200):
      word = random.choice(mimic_dict[word])
      mimic_words.append(word)

  return ' '.join(mimic_words)


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print(print_mimic(dict, ''))


if __name__ == '__main__':
  main()
