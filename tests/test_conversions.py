#!/usr/bin/env python
"""
    tests.test_conversions
    ~~~~~~~~~~~~~~~~~~~~~~

    Tests for the conversions module.

    :copyright: 2019 Eddy van den Aker (eddy.v.d.aker@gmail.com,
        eddy.vandenaker@zuyd.nl)
    :license: MIT
"""
from binary_practice.conversions import to_binary


class TestToBinary:
    """Tests for the to_binary function."""

    def test_to_binary(self):
        """Tests the to_binary function."""
        expected = '1000001'
        assert to_binary(65) == expected

        expected = '11111110'
        assert to_binary(254) == expected

        expected = '10001111'
        assert to_binary(143) == expected

        expected = '1000'
        assert to_binary(8) == expected
