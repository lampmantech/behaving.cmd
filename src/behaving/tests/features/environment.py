import os
from behaving.cmd import environment as cenv


def before_all(context):
    import behaving
    cenv.before_all(context)


def after_all(context):
    cenv.after_all(context)


def before_feature(context, feature):
    cenv.before_feature(context, feature)


def after_feature(context, feature):
    cenv.after_feature(context, feature)


def before_scenario(context, scenario):
    cenv.before_scenario(context, scenario)


def after_scenario(context, scenario):
    cenv.after_scenario(context, scenario)
