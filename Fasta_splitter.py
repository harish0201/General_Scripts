#!/usr/bin/env python
import sys
"""
usage: python Fasta_splitter.py genome.fasta 2> /dev/null
"""
f=open(sys.argv[1],"r");
opened = False
for line in f :
  if(line[0] == ">") :
    if(opened) :
      of.close()
    opened = True
    of=open("%s.fa" % (line[1:].rstrip()), "w")
    print(line[1:].rstrip())
  of.write(line)
of.close()
