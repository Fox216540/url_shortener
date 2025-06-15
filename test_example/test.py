from pyexpat.errors import messages

import pytest
import time

def square(n: int):
    return n * n 

def test_square_1():
    assert square(5) == 25

def test_square_2():
    assert square(7) == 49


def test_square_3_failed():
    assert square(1) == 25


@pytest.mark.parametrize("n, squared", [
    (5, 25),
    (10, 100),
    (1, 1)
])
def test_square(n: int, squared: int):
    assert square(n) == squared


@pytest.mark.slow
def test_slow_square():
    time.sleep(2)
    assert True



class Error(Exception):
    message = None

    def init(self, message=None):
        if message is None:
            message = self.message
        super().init(message)


class RepoError(Error):
    message = "RepoError: "

class AddMailRepoError(RepoError):
    def get_error_message(self):
        message = self.message + "Failed to add mail in repo"
        return message

class AddMailOfCrLsAgRepoError(RepoError):
    message = "Failed to add mail of cr ls ag in repo"

class QuestionRepoError(RepoError):
    message = "Question does not exist in repo"

class QuestionNotFoundRepoError(RepoError):
    message = "Question for this language or country doesn't exist in repo"




