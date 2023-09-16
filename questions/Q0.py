"""
Question goes here
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = "Answer goes here"


@lib.profiling.profileit()
def main() -> int:
    """
    """


if __name__ == "__main__":

    answer = main()
