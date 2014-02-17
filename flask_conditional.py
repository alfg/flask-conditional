"""
flask.ext.conditional
==================

This module provides conditional decorators for Flask routes.

:copyright: (C) 2014 by Alfred Gutierrez.
:license:   MIT, see LICENSE for more details.
"""


class conditional(object):
    """
    A conditional decorator utility.
    """
    def __init__(self, decorator, condition):
        self.decorator = decorator
        self.condition = condition

    def __call__(self, func):
        if not self.condition:
            return func
        return self.decorator(func)
