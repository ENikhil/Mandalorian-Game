import numpy as np
import sys
from terminal import getTerminalSize
#from getch import _getChUnix

sys.stdout.write("\x1b[%d;%df%s" % (10, 9, 'l'*3))
sys.stdout.flush()
