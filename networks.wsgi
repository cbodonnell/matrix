#!/media/PI-EXT/web/networks/venv/bin/python3

activate_this = '/media/PI-EXT/web/networks/venv/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/media/PI-EXT/web/networks/")
sys.path.insert(0,"/media/PI-EXT/web/networks/networks")

from networks import app as application