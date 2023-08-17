# conftest

conftest.py:
    def pytest_runtest_setup(item):
        # called for running each test in 'a' directory
        print ("setting up", item)

test_sub.py:
    def test_sub():
        pass

test_flat.py:
    def test_flat():
        pass

# Here is how you might run it:

py.test test_flat.py   # will not show "setting up"
py.test a/test_sub.py  # will show "setting up"

---------------------------------------------------------------------------------------------
# hooks
# Pytest hooks == event handlers

# Create new hook
import pytest

@pytest.mark.hookwrapper
def pytest_pyfunc_call(pyfuncitem):
    # do whatever you want before the next hook executes
    outcome = yield
    # outcome.excinfo may be None or a (cls, val, tb) tuple
    res = outcome.get_result()  # will raise if outcome was exception
    # postprocess result

# Default hooks
def pytest_sessionstart(session):
    # setup_stuff
def pytest_sessionfinish(session, exitstatus):
    # teardown_stuff

def pytest_addoption(parser):
    """
    @brief  Plugin specific options.
    """
    parser.addoption("--repeat", type="int", default=0, dest="repeat",
                     help="Run test the specified number of times") # config.option.repeat

pytest_configure(config)
    called after command line options have been parsed and all plugins and initial conftest files been loaded.

pytest_unconfigure(config)

pytest_runtest_setup(item)
    called before pytest_runtest_call(item).

pytest_runtest_call(item)
    called to execute the test item.

pytest_runtest_teardown(item, nextitem)
    called after pytest_runtest_call.
---------------------------------------------------------------------------------------------
# fixtures

# But actually next fixture with session scope looks much prettier:
@fixture(autouse=True, scope='session')
def my_fixture():
    # setup_stuff
    yield
    # teardown_stuff

# content of conftest.py
import smtplib
import pytest
@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()

    request.addfinalizer(fin)
    return smtp_connection  # provide the fixture value

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0 # for demo purposes

---------------------------------------------------------------------------------------------
# plugins

# sample ./setup.py file
from setuptools import setup

setup(
    name="myproject",
    packages=["myproject"],
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["name_of_plugin = myproject.pluginmodule"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)

# OR - in conftest.py
pytest_plugins = ['core.plugins.pytest_repeat_run']

# And in plugin module
def pytest_configure(config):
    """
    @brief  Registering plugin.
    """
    if config.option.repeat:
        config.pluginmanager.register(RepeatRun(config), "pytest_repeat_run")

# py.test --traceconfig - all plugins
plugin = config.pluginmanager.getplugin("name_of_plugin")


