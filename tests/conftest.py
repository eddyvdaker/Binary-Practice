import pytest

from binary_practice.questions import Question

@pytest.fixture
def question():
    return Question(8, '1000', 'Convert 8 to binary')


@pytest.fixture
def question_decimal_to_binary(question):
    return question


@pytest.fixture
def question_binary_to_decimal():
    return Question('1000', 8, 'Convert 1000 to deicmal')
