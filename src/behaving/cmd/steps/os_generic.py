## -*-mode: python; fill-column: 75; encoding: utf-8; coding: utf-8-unix -*-
"""
This file should work on any OS as the tests use Python commands.
"""

import sys
import os
import time

from behave import step

@step(u'I sleep for "{uSec}" seconds')
def zI_sleep_for_seconds(context, uSec):
    time.sleep(float(uSec))
    
@step(u'Assert that the directory "{uDir}" exists')
@step(u'Assert the directory "{uDir}" exists')
def bAssert_the_directory_exists(context, uDir):
    uDir = os.path.expandvars(uDir)
    assert os.path.exists(uDir), "os.path.exists(%r)" % (uDir,)
    # This follows symbolic links
    assert os.path.isdir(uDir), "os.path.isdir(%r)" % (uDir,)
    return True

@step(u'Ensure the directory "{uDir}" exists')
@step(u'Ensure that the directory "{uDir}" exists')
def bEnsure_the_directory_exists(context, uDir):
    uDir = os.path.expandvars(uDir)
    if os.path.isdir(uDir): return True
    if os.path.exists(uDir):
        # dead symlink et.al.
        raise RuntimeError("os.path.exists(%r) but is not a directory" % (uDir,))
    os.makedirs(uDir)
    return os.path.isdir(uDir)

