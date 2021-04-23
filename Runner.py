#!/usr/bin/env python3

import marshal
import sys
import os

#my code imports
import Read
import Parse
import PreProcess
import CodeContext
import Compile

#ugly af lmao
def main():
    fname = sys.argv[1]
    read = Read.read(fname)
    all_objs = [[n] for n in Parse.split(read)] #objects are mapped to array so that we can use the pass by reference nature of the array to handle objects referencing other objects
    [PreProcess.PreProcess(n[0], all_objs) for n in all_objs] 
    oname, _ = os.path.splitext(fname)
    oname += ".pyc"
    for n in all_objs:
        n[0] = n[0].MakePyObj() #references
    Compile.Out(oname, next(n[0] for n in all_objs if n[0].co_name.upper() == "MAIN"))
main()

"""
ok so wait

the problem is that its trying to marshal a codecontext
    - fucking circular dependecies i swaer to god

so we need to compile the objects first before we compile them
    - if we had pointers this would be wayyy fucking easier but we can't
        - cause no pointers oh my god what do i fucking do
        some funky scope shit i gujess

    """
