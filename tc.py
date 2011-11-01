#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(
       description = 'Converts HH:MM:SS to seconds or seconds'
       'to HH:MM:SS')

parser.add_argument ('input', help='This argument must be a string in'
'HH:MM:SS format or a number representing seconds.')

results = parser.parse_args()

# Convert from HH:MM:SS to milliseconds
if (results.input.find(":") != -1):
   input_split = [int(s) for s in results.input.split(':')]

   if (len(input_split) != 3):
       raise Exception("Must be in format HH:MM:SS")

   seconds = input_split[0]*3600 + input_split[1]*60 + input_split[2]

   print seconds

# Convert from milliseconds to HH:MM:SS
else:
   seconds = int(results.input)
   h = seconds / (60 * 60);
   m = (seconds / 60) % 60;
   s = seconds % 60;

   print '%02d:%02d:%02d' % (h, m, s)
