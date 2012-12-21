#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import tempfile
import unittest
import logging

## logging
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

class MyLogHandler(logging.Handler):
    def emit(self, record):
        pass

logging.getLogger().addHandler(MyLogHandler())

# Path hack.

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(1, os.path.abspath('../lib/'))
#print sys.path
import salesking

# More hacks
sys.path.append('.')
from salesking.tests import *

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)
    

if __name__ == '__main__':
    unittest.main()