#!/usr/bin/python3
# -*- coding: utf-8 -*-



import random

#: Black
black = (0,0,0)
#: White
white = (255,255,255)
#: Red
red   = (255,0,0)
#: Green
green = (0,255,0)
#: Blue
blue  = (0,0,255)

def randcol():
    """return a random color.

    :returns: a random color"""
    return ( random.randint(0,255),
             random.randint(0,255),
             random.randint(0,255) )
