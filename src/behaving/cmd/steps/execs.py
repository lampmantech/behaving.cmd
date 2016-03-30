## -*-mode: python; fill-column: 75; encoding: utf-8; coding: utf-8-unix -*-
"""
This file is Unix only for the moment; it requires the sh Python package.
It may work on Windwoes if the pbs Python package is installed.

This file will get imported, and if you don't have sh/pbs installed,
the import will succeed, but the steps requiring it won't work.
"""

import sys
import os

from behave import step

if not sys.platform.startswith('win'):
    try:
        import sh
    except ImportError:
        sh = None
else:
    try:
        # untested - pro forma
        import pbs as sh
    except ImportError:
        sh = None

@step(u'Assert the executable "{uExe}" exists on the PATH')
def zAssert_the_executable_exists(context, uExe):
    """
	Assert the executable "{uExe}" exists on the PATH
    """
    if os.path.isabs(uExe):
        uExe = os.path.realpath(uExe)
        assert (os.path.exists(uExe) and
                    os.access(uExe, os.X_OK) and
                    os.path.isfile(uExe)), \
                    'zAssert_the_executable_exists: ' +uExe
        return uExe
    assert sh, "This step requires the sh Python package"
    from sh import which
    sRetval = which(uExe)
    assert sRetval, 'zAssert_the_executable_exists: ' +uExe
    return sRetval
    
@step(u'Assert the background command "{uExe}" returns 0 with |argument| following')
def vAssert_execute_the_background_command(context, uExe):
    """
    Execute the background command "{uExe}" with |argument| following
    | argument |

    Takes a table of arguments that are used by the command,
    and runs the command in the background.

    The arguments can start with '>' '2>' and '<' to redirect stdout, 
    stderr, and stdin to or from files that are the rest of the agument.
    """
    
    iAssert_execute_the_command_table(context, uExe, bBg=True)
    # Signals will not raise an ErrorReturnCode. The command will return as if
    # it succeeded, but its exit_code property will be set to -signal_num.
    assert iRetval == 0, "Non-zero exit code for %s: %d" % (
        uExe, iRetval)
    return iRetval
    
@step(u'Execute the command "{uExe}" with |argument| following')
@step(u'Assert the command "{uExe}" returns 0 with |argument| following')
def vAssert_execute_the_command(context, uExe):
    """
    Execute the background command "{uExe}" with |argument| following
    | argument |

    Takes a table of arguments that are used by the command.

    The arguments can start with '>' '2>' and '<' to redirect stdout, 
    stderr, and stdin to or from files that are the rest of the agument.
    """
    
    iAssert_execute_the_command_table(context, uExe, bBg=False)
    # Signals will not raise an ErrorReturnCode. The command will return as if
    # it succeeded, but its exit_code property will be set to -signal_num.
    assert iRetval == 0, "Non-zero exit code for %s: %d" % (
        uExe, iRetval)
    return iRetval
    
@step(u'Execute the command "{uExe}" with arguments "{uArgs}"')
@step(u'Assert the command "{uExe}" returns 0 with arguments "{uArgs}"')
def iAssert_execute_the_command_string(context, uExe, uArgs):
    """
    Execute the command "{uExe}" with arguments "{uArgs}"
    """
    # FixMe: shell lex split
    lArgs = uArgs.split()
    dKw = {}
    iRetval = iAssert_execute_the_command(context, uExe, *lArgs)
    # Signals will not raise an ErrorReturnCode. The command will return as if
    # it succeeded, but its exit_code property will be set to -signal_num.
    assert iRetval == 0, "Non-zero exit code for %s: %d" % (
        uExe, iRetval)
    return iRetval
    
@step(u'Execute the background command "{uExe}" with arguments "{uArgs}"')
def iAssert_execute_the_command_string(context, uExe, uArgs):
    """
    Execute the command "{uExe}" with arguments "{uArgs}"
    """
    # FixMe: shell lex split
    lArgs = uArgs.split()
    dKw = {}
    dKw['_bg'] = True
    iRetval = iAssert_execute_the_command(context, uExe, *lArgs)
    # Signals will not raise an ErrorReturnCode. The command will return as if
    # it succeeded, but its exit_code property will be set to -signal_num.
    assert iRetval == 0, "Non-zero exit code for %s: %d" % (
        uExe, iRetval)
    return iRetval
    
def iAssert_execute_the_command_table(context, uExe, bBg=False):
    
    lArgs = []
    dKw = {}
    sIn = None
    if bBg: dKw['_bg'] = bBg
    for row in context.table:
        uElt = row['argument']
        # not uElt.startswith('>>')
        if uElt.startswith('1>'):
            dKw['_out'] = uElt[2:]
        elif uElt.startswith('>'):
            dKw['_out'] = uElt[1:]
        elif uElt.startswith('2>'):
            dKw['_err'] = uElt[2:]
        elif uElt.startswith('<'):
            dKw['_in'] = uElt[1:]
        else:
            lArgs.append(uElt)
    iRetval = iAssert_execute_the_command(context, uExe, *lArgs, **dKw)
    # Signals will not raise an ErrorReturnCode. The command will return as if
    # it succeeded, but its exit_code property will be set to -signal_num.
    assert iRetval == 0, "Non-zero exit code for %s: %d" % (
        uExe, iRetval)
    return iRetval

def iAssert_execute_the_command(context, uExe, *lArgs, **dKw):
    assert sh, "This step requires the sh Python package"
    sExe = zAssert_the_executable_exists(context, uExe)
    
    oCmd = sh.Command(sExe)
    if '_in' not in dKw:
        dKw['_in'] = None
    elif dKw['_in']:
        dKw['_in'] = open(dKw['_in'], 'r')
    # If a process ends with an error, an exception is generated dynamically.
    try:
        oRetval = oCmd(*lArgs, **dKw)
    finally:
        if dKw['_in']: dKw['_in'].close()

    return oRetval.exit_code

@step(u'Assert the command "{uExe}" returns non-zero with arguments "{uArgs}"')
def iAssert_the_command_string_returns_non_zero(context, uExe, uArgs):
    """
    
    """
    # FixMe: shell lex split
    lArgs = uArgs.split()
    dKw = {}
    iRetval = iAssert_execute_the_command(context, uExe, *lArgs)
    # Signals will not raise an ErrorReturnCode. The command will return as if
    # it succeeded, but its exit_code property will be set to -signal_num.
    assert iRetval > 0, "Zero exit code for %s: %d" % (
        uExe, iRetval)
    return iRetval

    
