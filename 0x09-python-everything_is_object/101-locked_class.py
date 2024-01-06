#!/usr/bin/python3
""" define a class LockedClass """

class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """ creates a new instance """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
