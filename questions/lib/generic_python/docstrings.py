"""
Things relating to object docstrings.
"""

from functools import wraps


def generate_docstring_decorator(docstring_template: str):
    """
    Create a decorator which assigns a docstring template to an object.
    """

    def format_docstring(*docstring_args, **docstring_kwargs):
        """
        Format the docstring template to be specific to this object.
        """

        def decorator(obj):

            @wraps(obj)
            def wrapper(*args, **kwargs):

                return obj(*args, **kwargs)

            wrapper.__doc__ = docstring_template.format(*docstring_args, **docstring_kwargs)

            return wrapper

        return decorator

    return format_docstring
