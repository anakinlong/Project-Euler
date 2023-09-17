"""
Things relating to object docstrings.
"""

from functools import wraps
from typing import Any


def generate_docstring_decorator(base_docstring: str):
    """
    Create a decorator which assigns a given docstring to the object.
    """

    def format_docstring(*args, **kwargs):
        """
        Format the base docstring to be specific to this object.
        """

        def decorator(func):

            @wraps(func)
            def wrapper(obj: Any):
                obj.__doc__ = base_docstring.format(*args, **kwargs)

                return obj

            return wrapper

        return decorator

    return format_docstring
