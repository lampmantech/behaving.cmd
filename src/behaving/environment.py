from behaving.cmd import environment as cmdenv

# We pull in the personae as we'll probably make use of them to deal
# with multi-user, and as a check that we are working with behaving.
from behaving.personas import environment as personaenv


def before_all(context):
    cmdenv.before_all(context)
    personaenv.before_all(context)
    context.config.log_capture = False


def after_all(context):
    cmdenv.after_all(context)
    personaenv.after_all(context)


def before_feature(context, feature):
    cmdenv.before_feature(context, feature)
    personaenv.before_feature(context, feature)


def after_feature(context, feature):
    cmdenv.after_feature(context, feature)
    personaenv.after_feature(context, feature)


def before_scenario(context, scenario):
    cmdenv.before_scenario(context, scenario)
    personaenv.before_scenario(context, scenario)


def after_scenario(context, scenario):
    cmdenv.after_scenario(context, scenario)
    personaenv.after_scenario(context, scenario)
