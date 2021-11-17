import os

import pytest


dirname = os.path.dirname(__file__)


@pytest.fixture
def episode_1_file():
    return os.path.join(dirname, "./fixture-ep-1.txt")


@pytest.fixture
def episode_2_file():
    return os.path.join(dirname, "./fixture-ep-2.txt")


@pytest.fixture
def episode_3_file():
    return os.path.join(dirname, "./fixture-ep-3.txt")
