#!/usr/bin/python3
# -*- coding: utf-8 -*-



from math import sqrt

def distance(coord1, coord2):
    """
    return the distance between two points

    :param coord1: a plane coordinate
    :type coord1: couple
    :param coord2: a plane coordinate
    :type coord2: couple
    :returns: the euclidean distance between coord1 and coord2
    :UC: None
    """

    x1,y1 = coord1
    x2,y2 = coord2
    return sqrt( (x1-x2)**2 + (y1-y2)**2 )


def are_number_close(r1,r2,tol):
    """
    check whether the relative error between two positive numbers is
    less than a given tolerance

    :param r1: a number
    :type r1: numeric
    :param r2: a number
    :type r2: numeric
    :param tol: the tolerance
    :type tol: float
    :rtype: boolean
    :returns: True is the relative error between r1 and r2 is less than tol

    :UC: r1>=0, r2>=0, r1 or r2 is >0, and 0.0<=tol<=1.0
    """

    assert ((type(r1)==int or type(r1)==float) and
            (type(r2)==int or type(r2)==float)), \
            "numeric types expected for the two numbers"

    assert type(tol)==float, "tolerance should be a float"

    assert (r1>=0) and (r2>=0) and \
        (r1>0 or r2>0), "invalid numbers"
    assert (0.0<=tol<=1.0), "the tolerance should be between 0.0 and 1.0"

    return (abs( (r1-r2)/(r1+r2) ) < tol)
