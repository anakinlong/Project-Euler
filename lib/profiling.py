"""
A code profiler.
"""

from time import monotonic
from functools import wraps
import logging
import inspect
from typing import Any, Callable


def profileit(
    template: str = "`{_function}` completed in {_time}.",
    level: int = logging.INFO,
    init_template: str | None = None,
    log_result: bool = False,
):
    """
    A code profiler - this times the execution of the code it wraps.

    :param template: the template for the message which is logged once the function has finished running.
    Defaults to `{_function} completed in {_time}.`.
    :param level: the logging level of the logs this decorator produces. Defaults to INFO.
    :param init_template: if provided, a message of this format will be logged when execution of the function begins.
    Defaults to None.
    :param log_result: whether or not to log the return value of the function. Defaults to False.
    """
    def decorator(func: Callable[[Any], Any]):
        # Get the signature of the decorated function:
        signature = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Start the clock:
            m = monotonic()
            func_failed = False

            # Inspect the function being called with the args passed:
            func_bound = signature.bind(*args, **kwargs)
            # Apply any defaults to the call for keyword arguments that have not been set:
            func_bound.apply_defaults()

            # Attempt to execute the function with the given arguments:
            try:
                # If an init_template has been given, print a message using it:
                if init_template:
                    logging.getLogger(func.__module__).log(
                        level,
                        "profiling: "
                        + init_template.format(
                            # Pass the arguments in:
                            *func_bound.args,
                            **func_bound.kwargs,
                            # Profiling information:
                            _function=func.__name__,
                        ),
                    )
                # Run the function:
                result = func(*args, **kwargs)

                return result

            # If we run into an error, raise it:
            except Exception as e:
                func_failed = True
                result = None
                raise e

            # Before the result is returned or error is raised:
            finally:
                if not func_failed:
                    logging.getLogger(func.__module__).log(
                        level,
                        "profiling: "
                        + template.format(
                            # Pass the arguments in:
                            *func_bound.args,
                            **func_bound.kwargs,
                            # Profiling information:
                            _function=func.__name__,
                            _time=f"{monotonic() - m:.2f}s",
                            _result=result,
                        ),
                        extra={"details": result} if log_result else {},
                    )

        return wrapper

    return decorator
