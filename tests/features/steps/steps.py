"""
The steps {{{features/steps/}}} module is where you import the steps code from
other behaving packages. For example, to use {{{behaving.cmd}}} in your steps,
you would add a line like:
{{{
    from behaving.cmd.steps import *
}}}
"""

from behave import *

from behaving.cmd.steps import *

from behaving.personas.steps import *
from behaving.personas.persona import persona_vars
