#!/usr/bin/python3
""" define a class LockedClass"""


class LockedClass:
    """ LockedClass"""
    __slot__ = ["first_name"]

    def __int__(self):
        """ creates a new instances """
        self.firstname = "first_name"
