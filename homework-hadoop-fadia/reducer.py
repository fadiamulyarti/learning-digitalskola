
#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# read the entire line from STDIN
for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # splitting the data on the basis of tab we have provided in mapper.py
  word, count = line.split('\t', 1)
  try:
    count = int(count)
  except ValueError:
    continue

  if current_word == word:
    current_count += count
  else:
    if current_word: #to not print current_word=None
      print('%s\t%s' % (current_word, current_count))
    current_count = count
    current_word = word

# do not forget to output the last word if needed!
if current_word == word:
  print('%s\t%s' % (current_word, current_count))
