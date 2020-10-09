#!/usr/bin/env python3

activate_this = '/var/www/networks/venv/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/networks/")
sys.path.insert(0,"/var/www/networks/networks")

from networks import app as application