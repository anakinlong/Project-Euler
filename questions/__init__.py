"""
The code for each question.
"""

# Here we do some magic so that we can do import all the modules in this directory without explicitly typing each one.
# This is slightly risky, since adding one question file with an error would cause everything to crash.

from os.path import dirname, basename, isfile, join
import glob
import re

# First we create a list of all files in the same directory as this __init__ file which end in .py:
modules = glob.glob(join(dirname(__file__), "*.py"))
# Then we assign the list of all those file names, without the .py suffix, which:
# a) are actually files
# b) are not this file
# c) have names of the form Q{n}.py, where n is an integer
# to the __all__ variable:
pattern = r'Q(\d+)\.py'
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and re.match(pattern, basename(f)) and not f.endswith('__init__.py')
]

# Now when we import everything, those modules will be imported:
from . import *  # NOQA

# Create a list of the question numbers which have files by removing the Q and turning the rest into an integer:
QUESTION_NUMBERS = [int(module[1:]) for module in __all__]
