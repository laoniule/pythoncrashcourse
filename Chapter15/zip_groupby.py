#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   zip_groupby.py
@Time    :   2019/09/24 09:55:52
@Author  :   Niu Xiaodong 
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib

from itertools import groupby

a=["x","y","z"]
b=[1,2,3]
c=["a","b","c","d"]
abzip=zip(a,b,c)
#print(list(abzip))
#print(dict(abzip))

#for key,group in groupby(sorted(abzip),lambda x:x[0]):
#    print(key,list(group))

g=groupby(sorted(abzip),lambda x:x[0])
print(list(g))