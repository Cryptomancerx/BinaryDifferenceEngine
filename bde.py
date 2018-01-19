#Written by Ben Greenberg using Python 3.6.4
#The Binary Difference Engine (BDE) compares a number of bytes from a given offset for a set of files to determine the maximally overlapping possible YARA-style signature that will trigger on every file within the set.
#Requires: none

#Usage:
#bde.py [-h] [-o OFFSET] -n NUMBYTES -f FILELIST [FILELIST ...]

#Usage examples:
#bde.py -n 100 -f file1, file2, file3 -> Create a 100 byte YARA-style signature for three files from the start of the files.
#bde.py -n 250 -o 10 -f file1, file2 -> Create a 250 byte YARA-style signature for two files starting from a 10 byte offset. Offsets are decimal, not hex

import argparse

def Main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-o", help="Specifies how many bytes to skip from the start of the file before reading. Defaults to 0.\n", dest="offset", type=int, default=0)
  parser.add_argument("-n", help="Specifies how many bytes to read from the given offset.\n", dest="numbytes", type=int, required=True)
  parser.add_argument("-f", nargs="+", help="List of files to compare. Provide at least 2.", dest="filelist", required=True)
  args = parser.parse_args()

  bytestringarray = []
  print()

  for x in range(0, len(args.filelist)): #Loop through all files, store data in byte strings, and print byte strings.
    with open(str(args.filelist[x]),"rb") as bdefile:
      bdefile.seek(args.offset)
      bytestringarray.append(bdefile.read(args.numbytes))
    
    print(args.filelist[x])
    for y in range(0, len(bytestringarray[x])):
      print(format(bytestringarray[x][y], "02X"), end=" ")
    print("\n")
    
  signaturestring = list(bytestringarray[0]) #Initialize signature string by setting it equal to the first byte string.

  for x in range(1, len(args.filelist)): #Loop through remaining byte strings, comparing byte-by-byte. If a value doesn't match, set that value in the signature string to "??".
    for y in range(0, args.numbytes):
      if signaturestring[y] == bytestringarray[x][y]:
        continue
      else:
        signaturestring[y] = "??"
        
  print("YARA-style signature string: ") #Print out our YARA-style signature string
  for x in range(0, args.numbytes):
    if signaturestring[x] != "??":
      print(format(signaturestring[x], "02X"), end=" ")
    else:
      print(signaturestring[x], end=" ")

if __name__ == "__main__":
  Main()