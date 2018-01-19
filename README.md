# BinaryDifferenceEngine

Written by Ben Greenberg using Python 3.6.4

The Binary Difference Engine (BDE) compares a number of bytes from a given offset for a set of files to determine the maximally overlapping possible YARA-style signature that will trigger on every file within the set.  

Requires: none  

Usage:  
bde.py [-h] [-o OFFSET] -n NUMBYTES -f FILELIST [FILELIST ...]  

Usage examples:  
bde.py -n 100 -f file1, file2, file3 -> Create a 100 byte YARA-style signature for three files from the start of the files.  
bde.py -n 250 -o 10 -f file1, file2 -> Create a 250 byte YARA-style signature for two files starting from a 10 byte offset. Offsets are decimal, not hex  
