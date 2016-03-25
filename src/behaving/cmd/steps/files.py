## -*-mode: python; fill-column: 75; encoding: utf-8; coding: utf-8-unix -*-

import sys
import os

from behave import step
from behaving.personas.persona import persona_vars

@step(u'Ensure the directory "{uDir}" exists')
def vEnsure_the_directory_exists(context, uDir):
    uDir = os.path.expandvars(uDir)
    assert os.path.exists(uDir), "os.path.exists(%r)" % (uDir,)
    # This follows symbolic links
    assert os.path.isdir(uDir), "os.path.isdir(%r)" % (uDir,)

@step(u'Ensure the file "{uFile}" exists')
def vEnsure_the_file_exists(context, uFile):
    uFile = os.path.expandvars(uFile)
    assert os.path.exists(uFile), "os.path.exists(%r)" % (uFile,)
    # This follows symbolic links
    assert os.path.isfile(uFile), "os.path.isfile(%r)" % (uFile,)

