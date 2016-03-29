## -*-mode: python; fill-column: 75; encoding: utf-8; coding: utf-8-unix -*-
"""
This file should work on any OS as the tests use Python commands.
"""

import sys
import os
import time

from behave import step

# These are just for proof of concept

@step(u'I sleep for "{uSec}" seconds')
def zI_sleep_for_seconds(context, uSec):
    time.sleep(float(uSec))
    
