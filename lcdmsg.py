#! /usr/bin/python
#coding: utf-8
#
import sys
argvs = sys.argv
argc  = len(argvs)

from PySensDevLibs.aqm1602 import AQM1602

aqm = AQM1602()
aqm.InitLCD()

if argc==1:
    print("You need parameters")
    sys.exit()

if argc==2:
    wl = " " * 16
    if argvs[1]=="U":
        aqm.moveTo(0,0)
        aqm.DisplayText(wl)
    elif argvs[1]=="D":
        aqm.moveTo(0,1)
        aqm.DisplayText(wl)
    else:
        aqm.clear()
        aqm.moveToHome()

if argc>=3:
    for i in range(1,argc):
        if argvs[i]=="U":
            i+=1
            aqm.moveTo(0,0)
            aqm.DisplayText(argvs[i])
        elif argvs[i]=="D":
            i+=1
            aqm.moveTo(0,1)
            aqm.DisplayText(argvs[i])
