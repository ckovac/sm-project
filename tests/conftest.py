# content of conftest.py
# adapted from http://pytest.org/latest/example/special.html

import pytest
import requests

def tear_down():
    ''' conftest.py tear_down - the last to go.... '''
    print("\nTEARDOWN after all tests")
    

@pytest.fixture(scope="session", autouse=True)
def set_up(request):
    ''' conftest.py set_up - the first to start.... '''

    print("\nSETUP before all tests")
    request.addfinalizer(tear_down)
