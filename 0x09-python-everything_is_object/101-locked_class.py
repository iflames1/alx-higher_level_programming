#!/usr/bin/python3
""" define a class LockedClass"""


class LockedClass:
    """define a class LockedClass"""

    def __setattr__(self, name: str, value) -> None:
        """check if the attribute is first_name"""

        if not hasattr(self, "first_name") and name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute "
                                 "'{}'".format(name))
        super().__setattr__(name, value)
