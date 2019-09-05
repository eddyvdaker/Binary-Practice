#!/usr/bin/env python
"""
    tests.test_generators
    ~~~~~~~~~~~~~~~~~~~~~

    Tests for the generators module.

    :copyright: 2019 Eddy van den Aker (eddy.v.d.aker@gmail.com,
        eddy.vandenaker@zuyd.nl)
    :license: MIT
"""
from binary_practice.generators import generate_number


class TestGenerateNumber:
    """Tests for the generate_number function."""

    def test_generate_number(self):
        """Test the generate_number function with default 
        arguments.
        """
        for i in range(100):
            actual = generate_number()
            expected_min = 0
            expected_max = 255
            assert actual >= expected_min and actual <= expected_max

    def test_generate_number_custom_max(self):
        """Tests the generate_number function with a custom max 
        value.
        """
        for i in range(100):
            actual = generate_number(max=10)
            expected_min = 0
            expected_max = 10
            assert actual >= expected_min and actual <= expected_max 

    def test_generate_number_custom_min(self):
        """Tests the generate_number function with a custom min 
        value.
        """
        for i in range(100):
            actual = generate_number(min=245)
            expected_min = 245
            expected_max = 255
            assert actual >= expected_min and actual <= expected_max

    def test_generate_number_custom_max_and_min(self):
        """Tests the generate_number function with both a custom min
        and custom max value.
        """
        for i in range(100):
            actual = generate_number(min=500, max=505)
            expected_min = 500
            expected_max = 505
            assert actual >= expected_min and actual <= expected_max

    def test_generate_number_ignore_list(self):
        """Tests the generate_number function with an ignore list."""
        for i in range(100):
            actual = generate_number(max=5, ignore=[1, 2, 3, 4])
            assert actual == 0 or actual == 5
