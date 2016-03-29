## -*-mode: python; fill-column: 75; encoding: utf-8; coding: utf-8-unix -*-

import sys
import os

from behave import step

# These are just for proof of concept
# Maybe use the vocabulary from RobotFramework:
#   Or add it as synonyms.
#   I don't like the aruba vocabulary.

@step(u'Assert that the directory "{uDir}" exists')
@step(u'Assert the directory "{uDir}" exists')
def bAssert_the_directory_exists(context, uDir):
    uDir = os.path.expandvars(uDir)
    assert os.path.exists(uDir), "os.path.exists(%r)" % (uDir,)
    # This follows symbolic links
    assert os.path.isdir(uDir), "os.path.isdir(%r)" % (uDir,)
    return True

@step(u'Assert that the file "{uFile}" exists')
@step(u'Assert the file "{uFile}" exists')
def bAssert_the_file_exists(context, uFile):
    uFile = os.path.expandvars(uFile)
    assert os.path.exists(uFile), "os.path.exists(%r)" % (uFile,)
    # This follows symbolic links
    assert os.path.isfile(uFile), "os.path.isfile(%r)" % (uFile,)
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

@step(u'Ensure the symlinks from the directory "{uDir}" exist with the |from|to| following')
def vEnsure_the_symlinks_in_the_directory(context, uDir):
    pass

@step(u'Write to the file "{uFile}" the lines following')
def vWrite_to_the_file_the_lines(context, uFile):
    pass

@step(u'Write to the file "{uFile}" with environ substitution the lines following')
def vWrite_to_the_file_with_environ(context, uFile):
    pass

@step(u'Write to the file "{uFile}" with context substitution the lines following')
def vWrite_to_the_file_with_context(context, uFile):
    pass

@step(u'Append to the file "{uFile}" the lines following')
def vAppend_to_the_file_the_lines(context, uFile):
    pass

@step(u'Append to the file "{uFile}" with environ substitution the lines following')
def vAppend_to_the_file_with_environ(context, uFile):
    pass

@step(u'Append to the file "{uFile}" with context substitution the lines following')
def vAppend_to_the_file_with_context(context, uFile):
    pass

@step(u'Ensure the file "{uFile}" is backed-up with the extension "{uExt}"')
def vEnsure_the_symlinks_in_the_directory(context, uFile, uExt):
    pass

