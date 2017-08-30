#!/usr/bin/python3

import re, sys, csv, datetime

try:
  file1 = sys.argv[1]
  file2 = sys.argv[2]
except IndexError:
  print("No files provided")
  quit()
