## -*-mode: python; fill-column: 75; encoding: utf-8; coding: utf-8-unix -*-

import sys
import os

from behave import step
from behaving.personas.persona import persona_vars

# These are just for proof of concept
# Maybe use the vocabulary from RobotFramework:
#   I don't like the aruba vocabulary.

@step(u'Assert the directory "{uDir}" exists')
def vAssert_the_directory_exists(context, uDir):
    uDir = os.path.expandvars(uDir)
    assert os.path.exists(uDir), "os.path.exists(%r)" % (uDir,)
    # This follows symbolic links
    assert os.path.isdir(uDir), "os.path.isdir(%r)" % (uDir,)

@step(u'Assert the file "{uFile}" exists')
def vAssert_the_file_exists(context, uFile):
    uFile = os.path.expandvars(uFile)
    assert os.path.exists(uFile), "os.path.exists(%r)" % (uFile,)
    # This follows symbolic links
    assert os.path.isfile(uFile), "os.path.isfile(%r)" % (uFile,)

# These are to help to define our vocabulary, even before coding it.

@step(u'Assert the file "{uFile}" contains the string "{uStr}"')
def vAssert_the_file_contains_string(context, uFile, uStr):
    pass

@step(u'Assert the file "{uFile}" contains the regexp "{uStr}"')
@step(u'Assert the file "{uFile}" contains the pyregexp "{uStr}"')
def vAssert_the_file_contains_pyregexp(context, uFile, uStr):
    pass

@step(u'Assert the directory "{uDir}" contains the file "{uFile}"')
def vAssert_the_directory_contains_file(context, uDir, uFile):
    pass

@step(u'Assert the directory "{uDir}" contains the glob "{uGlob}"')
def vAssert_the_directory_contains_glob(context, uDir, uGlob):
    pass

# FixMe: the inverses of the above

# FixMe: filenames in a table and the inverses of the above


