
#!/usr/bin/env python
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
  line = line.strip()
  # split the line into words, output data type list
  words = line.split()
  for word in words:
    print('%s\t%s' % (word, 1))
