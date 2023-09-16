"""
A code profiler.
"""

from time import monotonic, perf_counter
from functools import wraps
import inspect
from typing import Any, Callable


def profileit(
    template: str = "`{_function}`\nCompleted in {_time}.",
    init_template: str | None = None,
    log_result: bool = True,
    long_time: bool = False,
    decimal_places: int = 15,
):
    """
    A code profiler - this times the execution of the code it wraps.

    :param template: the template for the message which is printed once the function has finished running.
    Defaults to `{_function} completed in {_time}.`.
    :param init_template: if provided, a message of this format will be printed when execution of the function begins.
    Defaults to None.
    :param log_result: whether or not to print the return value of the function. Defaults to True.
    :param long_time: whether of not the function we are profiling will take a long time. Defaults to False.
    :param decimal_places: how many decimal places to which to round the total time. Defaults to 15.
    """
    # Use long_time to decide which timer to use to calculate the total time.
    # monotonic is better for long periods, perf_counter is better for short:
    current_time = monotonic if long_time else perf_counter

    def decorator(func: Callable[[Any], Any]):
        # Get the signature of the decorated function:
        signature = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Start the clock:
            start_time = current_time()
            func_failed = False

            # Inspect the function being called with the args passed:
            func_bound = signature.bind(*args, **kwargs)
            # Apply any defaults to the call for keyword arguments that have not been set:
            func_bound.apply_defaults()

            # Attempt to execute the function with the given arguments:
            try:
                # If an init_template has been given, print a message using it:
                if init_template:
                    print(
                        "Begin profiling: "
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
                    total_time = round(current_time() - start_time, decimal_places)
                    extra = f"\nResult: {result}" if log_result else ""
                    print(
                        "Finished profiling: "
                        + template.format(
                            # Pass the arguments in:
                            *func_bound.args,
                            **func_bound.kwargs,
                            # Profiling information:
                            _function=func.__name__,
                            _time=f"{total_time}s",
                            _result=result,
                        )
                        + extra,
                    )

        return wrapper

    return decorator
