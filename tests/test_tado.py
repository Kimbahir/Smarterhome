import pytest
import os
from TadoToolkit.tado import Tado

"""Run using python -m pytest
"""

# Fixtures


@pytest.fixture
def GetTado():
    tado_pass = os.environ['TADO_PASS']
    tado_email = os.environ['TADO_EMAIL']

    t = Tado(tado_email, tado_pass)
    return t


def test_initialization_email():
    with pytest.raises(Exception, match=r".*Email.*"):
        t = Tado("", "asdasdasd")


def test_initialization_password():
    with pytest.raises(Exception, match=r".*password.*"):
        t = Tado("foo@bar.com", "")


def test_get_bearer_token(GetTado):
    assert GetTado.get_bearer_token() == 200


def test_refresh_bearer_token(GetTado):
    assert GetTado.refresh_bearer_token() == 200


def test_get_home_id(GetTado):
    assert GetTado.get_home_id() == 200


def test_get_home_details(GetTado):
    assert GetTado.get_home_details() == 200


def test_get_presence(GetTado):
    assert GetTado.get_presence() == 200
