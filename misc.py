#import numpy as np
import sys
#from terminal import getTerminalSize
#from getch import _getChUnix
import random
import time as t
from firebeam import Beam
from grid import grid

beam = Beam(100, 10, "o", 1)

while(1):
    t.sleep(0.2)
    beam.update_loc(grid.matrix(), 'l', 1)
