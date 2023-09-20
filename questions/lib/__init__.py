"""
Useful functions/classes/constants etc. which can be used for multiple questions.
"""

# Add # NOQA after an import to stop IDE's complaining about unused imports/import * etc.

# The location of the "materials" directory - this contains any files required by some questions:
import pathlib
# Parent of this file is lib, parent of that is questions - materials directory is in there:
MATERIALS = pathlib.Path(__file__).parent.parent.joinpath("materials").resolve()
# Now the path to files in this directory can be found using lib.MATERIALS.joinpath("example.txt")

# Things which can be grouped nicely:
from . import factors  # NOQA
from . import fibonacci  # NOQA
from . import input_processing  # NOQA
from . import primes  # NOQA
from . import pandigital  # NOQA
from . import polygonal_numbers  # NOQA
from . import profiling  # NOQA

# Things which don't fit into a group:
from . import general  # NOQA
