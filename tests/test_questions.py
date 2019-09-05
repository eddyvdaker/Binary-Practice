#!/usr/bin/env python
"""
    tests.test_questions
    ~~~~~~~~~~~~~~~~~~~~

    Tests for the questions module.

    :copyright: 2019 Eddy van den Aker (eddy.v.d.aker@gmail.com,
        eddy.vandenaker@zuyd.nl)
    :license: MIT
"""
from binary_practice.questions import get_question, Question, \
    get_binary_to_decimal_question, get_decimal_to_binary_question, \
    DECIMAL_TO_BINARY, BINARY_TO_DECIMAL


class TestGetQuestion:
    """Tests for the get_question functions."""

    def test_get_question(self):
        """Tests get_question with default arguments."""
        got_binary_to_decimal = False
        got_decimal_to_binary = False
        for i in range(100):
            actual = get_question()
            if type(actual.answer) == str:
                got_decimal_to_binary = True
            else:
                got_binary_to_decimal = True
        assert got_binary_to_decimal and got_decimal_to_binary

    def test_get_question_decimal_to_binary(self):
        """Tests the get_question with DECIMAL_TO_BINARY as type."""
        got_binary_to_decimal = False
        got_decimal_to_binary = False
        for i in range(100):
            actual = get_question(question_type=DECIMAL_TO_BINARY)
            if type(actual.answer) == str:
                got_decimal_to_binary = True
            else:
                got_binary_to_decimal = True
        assert not got_binary_to_decimal and got_decimal_to_binary

    def test_get_question_binary_to_decimal(self):
        """Tests the get_question with BINARY_TO_DECIMAL as type."""
        got_binary_to_decimal = False
        got_decimal_to_binary = False
        for i in range(100):
            actual = get_question(question_type=BINARY_TO_DECIMAL)
            if type(actual.answer) == str:
                got_decimal_to_binary = True
            else:
                got_binary_to_decimal = True
        assert got_binary_to_decimal and not got_decimal_to_binary

    
class TestGetBinaryToDecimalQuestion:
    """Tests for the get_binary_to_decimal_question function."""
    
    def test_get_binary_to_decimal_question(self):
        """Test the get_binary_to_decimal_question function."""
        actual = get_binary_to_decimal_question()
        assert type(actual.answer) == int


class TestGetDecimalTobinaryQuestion:
    """Tests for the get_decimal_to_binary_question function."""
    
    def test_get_decimal_to_binary_question(self):
        """Test the get_decimal_to_binary_question function."""
        actual = get_decimal_to_binary_question()
        assert type(actual.answer) == str


class TestQuestion:
    """Tests for the Question class."""
    
    def test_question_creation(self):
        """Test the creation of Question objects."""
        question = Question(1, 2, 'text')
        assert question.number == 1
        assert question.answer == 2
        assert question.text == 'text'

    def test_question_render_question(self, question):
        """Test the render_question method."""
        expected = f'Convert {question.number} to binary:'
        actual = question.render_question()
        assert actual == expected

    def test_question_check_answer_binary_to_decimal(self,
            question_binary_to_decimal):
        """Test the check_answer method when the answer is in
        decimal.
        """
        answer = str(question_binary_to_decimal.answer)
        assert question_binary_to_decimal.check_answer(answer)

    def test_question_check_answer_binary_to_decimal_wrong(self,
            question_binary_to_decimal):
        """Test the check_answer method when the answer is in
        decimal and the answer is wrong.
        """
        assert not question_binary_to_decimal.check_answer(123456)

    def test_question_check_answer_decimal_to_binary(self,
            question_decimal_to_binary):
        """Test the check_answer method when the answer is in
        binary.
        """
        answer = str(question_decimal_to_binary.answer)
        assert question_decimal_to_binary.check_answer(answer)

    def test_question_check_answer_deciaml_to_binary_wrong(self,
            question_decimal_to_binary):
        """Test the check_answer method when the answer is in
        binary and the answer is wrong.
        """
        assert not question_decimal_to_binary.check_answer('1000000001')
