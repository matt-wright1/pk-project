"""pkmodel is a Pharmokinetic modelling library.

It contains functionality for creating, solving, and visualising the solution
of Parmokinetic (PK) models

"""
# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes and functions
from .compartments import *
#from .createmodel import *
from .dose import *
#from .inputs import *
from .model import *
#from .plot import *
from .solution import *
#from .solver import *

