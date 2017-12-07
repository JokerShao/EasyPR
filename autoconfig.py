#-*- coding:utf-8 -*-
# AUTHOR:   joker
# FILE:     autoconfig.py
# ROLE:     select opencv version & modify config.h 
# CREATED:  2017-12-07 15:58:03
# MODIFIED: 2017-12-07 17:20:24

import os
import re

version = os.popen('pkg-config --modversion opencv').readline().strip('\n')
number = filter(str.isdigit, version)
number_f3 = number[0:3]
diff = int(number_f3) - 320

if diff >= 0:
    configfile = open('./include/easypr/config.h', 'r')
    alllines = configfile.readlines()
    configfile.close()
    # print alllines
    configfile = open('./include/easypr/config.h', 'w+')
    current_line = 1
    for eachline in alllines:
        if current_line == 4:
            eachline = re.sub('ZERO', 'TWO', eachline)
        configfile.writelines(eachline)
        current_line += 1

