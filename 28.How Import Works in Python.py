# When we write a certain module name along with import keyword,
# it will start searching for a file with that name having an extension .py

import sys
print(sys.path)

''' The above code prints out the list of directories.
# When we command Python to import something,then it looks im each of the listed locations in order.'''

# Methods to import modules
# Classic way:-
import numpy

# Pick a specific resource
from bs4 import BeautifulSoup

# Rename while imported
import pandas as pd