#! /usr/bin/python

from collections import OrderedDict

vocabulary=OrderedDict()

vocabulary["C"]="a compile program language, linux was writed with it"
vocabulary["Python"]="a script language, Ops used it"
vocabulary["javascript"]="a script language, program dynamic web page"

for key,value in vocabulary.items():
    print(key+":"+value+"\n")



