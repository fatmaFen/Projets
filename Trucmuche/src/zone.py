#!/usr/bin/python3
# -*- coding: utf-8 -*-


import mathtools
def create(list_coords):
    """
    Constructor for a zone

    :param list_coords: a list of coordinates
    :type list_coords: list of couples
    :returns: a zone object
    :rtype: zone
    :UC: list_coords should not be empty
    """
    area=len(list_coords)
    xmoy=0
    ymoy=0
    moment=1
    for elt in list_coords:
          xmoy=xmoy+elt[0]
          ymoy=ymoy+elt[1]

    cg=(xmoy/area,ymoy/area)
    for coords in list_coords:
        moment+=mathtools.distance(coords,cg)**2

    zone={"coords":list_coords,"gravity":cg,"moment":moment,"area":area}
    return zone
def get_coords(z):
    """
    return the list of coordinates of the zone
    """
    return z["coords"]

def get_area(z):
    """
    return the area of the zone
    """

    return z["area"]

def get_cg(z):
    """
    return the centre of gravity of the zone
    """
    return zone["gravity"]

def get_moment(z):
    """
    return the moment of the zone
    """
    return z["moment"]


def are_similar(z1,z2,tol):
    """
    check whether the two zones are similar up to a tolerance

    :param z1: a zone
    :type z1: zone
    :param z2: another zone
    :type z2: zone
    :param tol: a tolerance
    :type tol: float
    :return: True if the two zones z1 and z2 are similar up to a tolerance.
    :rtype: boolean
    :UC: 0.0<=tol<=1.0
    """

    return mathtools.are_number_close(get_area(z1),get_area(z2),tol) and mathtools.are_number_close(get_moment(z1),get_moment(z2),tol)
