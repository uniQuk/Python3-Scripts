#!/usr/bin/python3

import subprocess
import re

# Retreive Process Data
pm = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0]
vu = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0]

# Iterate through the processes
pmTxt = pm.split(b'\n')
pmOut = re.compile(b'[\s]+')
rssTotal = 0  # kB
for row in range(1, len(pmTxt)):
    rowTxt = pmTxt[row].strip()
    rowEle = pmOut.split(rowTxt)
    try:
        rss = float(rowEle[0]) * 1024
    except:
        rss = 0  # ignore...
    rssTotal += rss

# Process Statistics
vuLines = vu.split(b'\n')
pmOut = re.compile(b':[\s]+')
vmOut = {}
for row in range(1, len(vuLines)-2):
    rowTxt = vuLines[row].strip()
    rowEle = pmOut.split(rowTxt)
    vmOut[(rowEle[0])] = int(rowEle[1].strip(b'\.')) * 4096

# Print Free Memory to terminal
print("Wired Memo: \t\t{} MB".format(vmOut[b"Pages wired down"]/1024/1034))
print("Active Memo: \t\t{} MB".format(vmOut[b"Pages active"]/1024/1024))
print('Inactive Mem:\t\t{} MB'.format(vmOut[b"Pages inactive"]/1024/1024))
print('Free Mem:\t\t\t{} MB'.format(vmOut[b"Pages free"]/1024/1024))
print('Real Mem Total:\t\t{}.3f MB'.format(rssTotal/1024/1024))
