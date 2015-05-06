from planterbox import (
    step,
    hook,
)


hooks_run = set()


@hook('before', 'feature')
def before_feature_hook(feature_suite):
    global hooks_run
    hooks_run.add(('before', 'feature'))


@hook('before', 'scenario')
def before_scenario_hook(scenario_test):
    global hooks_run
    hooks_run.add(('before', 'scenario'))


@hook('before', 'step')
def before_step_hook(step_text):
    global hooks_run
    hooks_run.add(('before', 'step'))


@step(r'I verify that all before hooks have run')
def verify_before_hooks(world):
    global hooks_run
    assert hooks_run == {('before', 'feature'),
                         ('before', 'scenario'),
                         ('before', 'step'),
                         }
