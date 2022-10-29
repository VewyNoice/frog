#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 02:03:02 2022

@author: charlottecook
"""

import time
import random
import statistics

machinetrials = 0

jumpnumbers = []

jumpspossible = int(input("How many destinations are there for our frog? "))
possibletargets = [1, jumpspossible]
usertrials = int(input("How many trials should there be? "))

starttime = time.time()
while machinetrials < usertrials:
    position = 0
    totaljumps = 0
    while position < jumpspossible:
        possibletargets[0] = position + 1
        position = random.randint((possibletargets[0]), (possibletargets[-1]))
        print (position)
        totaljumps = totaljumps + 1
    jumpnumbers.append(totaljumps)
    machinetrials = machinetrials + 1
    print()
endtime = time.time()

totaltime = endtime - starttime

print (f"Raw jumpnumbers list: {jumpnumbers}")
print()
print (f"{jumpspossible} possible destinations over {usertrials} trials.")
print()
print (f"Mean: {statistics.mean(jumpnumbers)}")
print (f"Mode: {statistics.mode(jumpnumbers)}")
print()
print (f"Time for code to execute: {totaltime} seconds")
print (f"rounded: {round(totaltime, 2)} seconds")
print()
print (f"or: {totaltime*10**3} milliseconds")
print (f"rounded: {round(totaltime*10**3, 2)} milliseconds")