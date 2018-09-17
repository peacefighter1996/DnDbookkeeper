# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:48:29 2018

@author: Ian-A
"""
import datetime
import warnings
import pytz
from tzlocal import get_localzone
float1 = 5.956252
float2 = 9812668161286.8712512
print ("ik ben data = {:6.3f}".format(float1))
print ("ik ben data = {},{:6.3f}".format(float1,float2))

print(get_localzone())
tz = pytz.timezone('US/Pacific')
def toUTC(d):
    return tz.normalize(tz.localize(d)).astimezone(pytz.utc)

print ("Test: ", datetime.datetime.utcnow(), " = ", toUTC(datetime.datetime.now()))